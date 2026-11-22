#!/usr/bin/env python3
"""Turn a `substack drafts export` file back into plain Markdown.

The export keeps each block as a base64 JSON comment (python-substack-node)
instead of readable text. This decodes those blocks, takes the title and
subtitle from the revision comment, and maps Substack image URLs back to the
local paths with the same alt text in LOCAL.md.

Usage: pull.py EXPORT.md LOCAL.md OUT.md
"""
import base64
import json
import re
import sys
from pathlib import Path

COMMENT = re.compile(r"<!-- python-substack-([a-z]+):v\d (\S+) -->\n?")
IMAGE = re.compile(r"!\[([^\]]*)\]\(([^)]+)\)")
ESCAPE = re.compile(r"\\([\\`*_{}\[\]()#+\-.!|>~<])")
# code blocks, code spans and node comments keep their backslashes
VERBATIM = re.compile(r"(```.*?```|`[^`\n]*`|<!-- python-substack-[^>]*-->)", re.S)


def _unescape(md):
    # blocks python-substack wrote itself export as escaped Markdown ("1\. Intro")
    parts = VERBATIM.split(md)
    return "".join(p if i % 2 else ESCAPE.sub(r"\1", p) for i, p in enumerate(parts))


def _decode(b64):
    return json.loads(base64.urlsafe_b64decode(b64 + "=" * (-len(b64) % 4)))


def _inline(nodes):
    out = ""
    for n in nodes or []:
        text = n.get("text", "")
        marks = {m["type"]: m for m in n.get("marks", [])}
        if "code" in marks:
            text = f"`{text}`"
        if "strong" in marks:
            text = f"**{text}**"
        if "em" in marks:
            text = f"*{text}*"
        if "link" in marks:
            text = f"[{text}]({marks['link']['attrs']['href']})"
        out += text
    return out


def _block(n):
    kind = n["type"]
    if kind == "paragraph":
        return _inline(n.get("content"))
    if kind == "heading":
        return "#" * n["attrs"]["level"] + " " + _inline(n.get("content"))
    if kind == "code_block":
        return f"```{n['attrs'].get('language') or ''}\n{_inline(n.get('content'))}\n```"
    if kind == "ordered_list":
        start = n["attrs"].get("start") or 1
        return "\n".join(f"{start + i}. {_block(li['content'][0])}" for i, li in enumerate(n["content"]))
    # shortcut: only the block types seen in exports so far; add new ones as they show up
    sys.exit(f"pull.py: unhandled block type {kind!r}, add it to _block()")


def pull(export_path, local_path, out_path):
    meta = {}

    def replace(m):
        if m[1] == "revision":
            meta.update(_decode(m[2]))
        if m[1] != "node":  # revision and image metadata
            return ""
        return _block(_decode(m[2])) + ("\n" if m[0].endswith("\n") else "")

    body = COMMENT.sub(replace, _unescape(Path(export_path).read_text(encoding="utf-8")))
    local = Path(local_path)
    local_imgs = dict(IMAGE.findall(local.read_text(encoding="utf-8"))) if local.exists() else {}
    body = IMAGE.sub(lambda m: f"![{m[1]}]({local_imgs.get(m[1], m[2])})", body)
    body = re.sub(r"\n{3,}", "\n\n", body).strip()
    head = f"# {meta.get('title', '')}\n\n" + (f"*{meta['subtitle']}*\n\n" if meta.get("subtitle") else "")
    Path(out_path).write_text(head + body + "\n", encoding="utf-8")
    return {"title": meta.get("title", ""), "subtitle": meta.get("subtitle", ""), "file": str(Path(out_path).resolve())}


if __name__ == "__main__":
    if len(sys.argv) != 4:
        sys.exit("usage: pull.py EXPORT.md LOCAL.md OUT.md")
    print(json.dumps(pull(*sys.argv[1:]), ensure_ascii=False))
