---
name: tldr
description: Use when the user types /tldr, "tldr", "tl;dr", "too long didn't read", "gist", "short version" or "summarize briefly", about the conversation so far, a long reply, a file, folder, URL, PR, branch, diff, log, command output or pasted text.
---

# TL;DR

A TL;DR is what the reader needs if they read nothing else. It is a selection, not a shorter rewrite: most of the source is left out on purpose.

## Find the target

| Input | Read |
|---|---|
| file / folder | the file; for a folder, its README and top-level layout |
| URL | fetch it; a claude.ai artifact link goes through the Artifact `read` action |
| PR number or URL, "this PR" | `gh pr view` and `gh pr diff` |
| branch, "my changes" | `git log main..HEAD`, `git diff main...HEAD --stat`, the key diffs |
| pasted text, logs, command output | that text |
| nothing, and the previous reply was long (150+ words) | that reply |
| nothing otherwise | the session: what was asked, what's done, where it stands |

## The reply

The reply is these lines, in this order, and nothing else:

1. **Bottom line.** One sentence, 25 words max: the verdict, the state, or the main point.
2. **Up to 3 bullets.** One line each, 15 words max, ranked by what changes the reader's next decision. Skip them if the bottom line covers it.
3. **`Next:`** One concrete action, only when the source implies one for the reader.

Total: 80 words max, however long the source is.

## Choosing what makes the cut

- Keep specifics: names, numbers, versions, paths, verdicts ("PR #50, 13 commits", not "several commits").
- Rank risks, blockers, decisions and deadlines above descriptions.
- Report only what the source says. If something is unclear, say so in a bullet.

## Example

Source: a 13-commit branch, 11.5k lines added. TL;DR:

```
`feat/dbml` adds DBML support to the CLI, editor and VS Code extension; PR #50 is open, versioned 0.2.0.
- `qdbd convert` turns QuickDBD into DBML and back, warning on anything lost.
- 7.2k of the 11.5k added lines are reference test fixtures.
- Extension 0.4.0 now requires `qdbd` 0.2.0 or newer.
```
