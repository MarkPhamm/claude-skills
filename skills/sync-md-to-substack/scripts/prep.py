#!/usr/bin/env python3
"""Prepare a Markdown post for python-substack.

The CLI keeps the "# Title" line in the body (so the title shows twice) and
resolves image paths against the current directory. This lifts the title and
an italic subtitle line out of the body and makes local image paths absolute.

Usage: prep.py POST.md OUT.md   -> prints {"title", "subtitle", "file"} as JSON
"""
import json
import re
import sys
from pathlib import Path

IMAGE = re.compile(r"(!\[[^\]]*\]\()([^)\s]+)")
SUBTITLE = re.compile(r"([*_])([^*_].*)\1")


def _drop_blank(lines):
    while lines and not lines[0].strip():
        lines.pop(0)


def prepare(md_path, out_path):
    src = Path(md_path).resolve()
    lines = src.read_text(encoding="utf-8").splitlines()
    _drop_blank(lines)
    title = subtitle = ""
    if lines and lines[0].startswith("# "):
        title = lines.pop(0)[2:].strip()
        _drop_blank(lines)
        match = SUBTITLE.fullmatch(lines[0].strip()) if lines else None
        if match:
            subtitle = match.group(2).strip()
            lines.pop(0)
            _drop_blank(lines)

    def absolute(m):
        target = m.group(2)
        if re.match(r"[a-zA-Z][a-zA-Z0-9+.-]*://", target) or target.startswith("/"):
            return m.group(0)
        return m.group(1) + str((src.parent / target).resolve())

    body = IMAGE.sub(absolute, "\n".join(lines) + "\n")
    out = Path(out_path)
    out.write_text(body, encoding="utf-8")
    return {"title": title, "subtitle": subtitle, "file": str(out.resolve())}


if __name__ == "__main__":
    if len(sys.argv) != 3:
        sys.exit("usage: prep.py POST.md OUT.md")
    print(json.dumps(prepare(sys.argv[1], sys.argv[2]), ensure_ascii=False))
