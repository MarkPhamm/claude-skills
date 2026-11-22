---
name: sync-md-to-substack
description: Use when the user asks to sync, push, upload or send a Markdown (.md) post to Substack, create a Substack draft from a file, update an existing Substack draft from a local file, or sync/pull a Substack draft back into a local .md file.
---

# Sync Markdown to Substack

Pushes a local `.md` post to Substack as a **draft**, using [python-substack](https://pypi.org/p/python-substack) through `uvx` (no install). It is unofficial and talks to Substack's private API, so it can break when Substack changes. Tested with 0.10.0.

Default publication: `https://markphammm.substack.com`. Ask only if the user names another one.

## Rules

- Drafts only. Never run `drafts publish`, `schedule`, `unschedule` or `delete` unless the user asks for that in the current turn.
- The login cookie never goes into a file, a commit or a memory. Prefer the user running the command in their own terminal (step 3).
- An update overwrites the draft body on Substack, including anything edited in Substack's editor. Ask before forcing it.

## 1. Prepare the file

```sh
python3 -I ~/.claude/skills/sync-md-to-substack/scripts/prep.py POST.md <scratchpad>/substack_post.md
```

It prints `{"title", "subtitle", "file"}`. Why: the CLI keeps the `# Title` line in the body, so the title shows twice, and it resolves image paths against the current directory. The script lifts out the `# Title` and an italic subtitle line right after it, and makes local image paths absolute. Empty `title` means the file has no `# ` line: ask for one.

## 2. New draft or update?

- New post: `drafts create`.
- The user gives a draft id or link (`.../publish/post/<id>`), or says "sync again": `drafts update <id>`. If unsure, list drafts first (`drafts list --json`) and match on title, so you don't create a duplicate.

## 3. Auth

Substack logs in with the `substack.sid` cookie (works for magic-link accounts, no password needed). To get it, in Chrome:

1. Open https://substack.com while logged in, press `Cmd + Option + I`.
2. **Application** tab → left sidebar **Storage → Cookies → `https://substack.com`**. Do not click "Clear site data" on the Storage page, it logs them out.
3. Filter `substack.sid`, double-click the **Value** cell, `Cmd + C`. It usually starts with `s%3A`.

**Preferred:** give the user the full command to run in their own terminal (zsh), so the cookie never enters the chat:

```sh
read -s "SID?substack.sid: " && export COOKIES_STRING="substack.sid=$SID" PUBLICATION_URL=https://markphammm.substack.com && \
uvx --from python-substack substack drafts create --title "<title>" --subtitle '<subtitle>' <file>
```

**If the user pastes the cookie into chat:** say it is now in the conversation log, use it as an inline env var on the command (`COOKIES_STRING='substack.sid=...' PUBLICATION_URL=... uvx ...`) for the syncs they ask for in this conversation, and tell them to log out of Substack when done to kill it. If it stops working (they logged out), fall back to the terminal command above.

## 4. Run it

Create:

```sh
uvx --from python-substack substack drafts create --title "<title>" --subtitle '<subtitle>' <file>
```

Prints `Created draft <id>: <title>`.

Update. It only replaces the body: the title stays, and in 0.10.0 `--subtitle` is silently ignored, so tell the user to change the subtitle in Substack's editor. The Bash tool is non-interactive, so `--yes` is required.

A local file that was not exported from the draft always needs three overrides: `--allow-conflict` (no revision metadata), `--allow-image-replacement` (local images have no markers) and `--allow-unsupported-change` (the exporter flags plain paragraphs and code blocks too). Together they overwrite the remote body, so check first:

1. Back up the remote draft: `drafts export <id> --output <scratchpad>/draft_<id>_backup.md`.
2. Compare its text with the local file. The node comments are base64 JSON (`python-substack-node:v1 <b64>`); decode them and collect the `text` fields. Also list node types: anything beyond `paragraph`, `heading`, `code_block`, lists and images (a button, an embed, a footnote) would be lost.
3. If the remote has text or nodes the local file lacks, show the user and ask before forcing. If not, go ahead.
4. Dry-run, then run:

```sh
uvx --from python-substack substack drafts update <id> <file> --allow-conflict --allow-image-replacement --allow-unsupported-change --dry-run --yes
uvx --from python-substack substack drafts update <id> <file> --allow-conflict --allow-image-replacement --allow-unsupported-change --yes
```

5. Verify: export again and check the links and text landed. Each sync re-uploads the local images as new files on Substack's CDN; harmless.

To pull Substack edits back into the local file instead, see step 6.

## 5. Report

- The draft link: `https://markphammm.substack.com/publish/post/<id>`.
- If the cookie was pasted in chat: remind them to log out of Substack.
- Ask them to check images, code blocks, tables and quotes in the editor; the Markdown conversion is not perfect.
- Any `[TODO]` markers in the post went up too.

## 6. Pull a draft back into the local file

`drafts export` does not give clean Markdown. Blocks touched in Substack's editor come out as base64 JSON comments (`python-substack-node:v1 <b64>`); blocks python-substack wrote come out as backslash-escaped Markdown (`## 1\. Intro`). The draft itself has no backslashes. `scripts/pull.py` handles both.

```sh
uvx --from python-substack substack drafts export <id> --output <scratchpad>/draft_pull.md --force
python3 -I ~/.claude/skills/sync-md-to-substack/scripts/pull.py <scratchpad>/draft_pull.md POST.md <scratchpad>/pulled.md
diff POST.md <scratchpad>/pulled.md
```

- Title and subtitle come from the export's revision comment. Updates never change the subtitle on Substack, so if the diff shows only the local one is newer, keep the local subtitle line.
- Images are mapped back to the local path with the same alt text. Images added in Substack's editor have no local copy and keep their Substack CDN URL; prep.py leaves URLs alone, so the next push still works.
- It handles paragraphs, headings, code blocks, bullet and ordered lists, images, and bold, italic, code and link marks. Any other block (quote, embed, button) stops it with `unhandled block type`: add a case to `_block()`.
- Show the user the diff before overwriting POST.md, unless it is clean in git. Then copy `pulled.md` over it.
