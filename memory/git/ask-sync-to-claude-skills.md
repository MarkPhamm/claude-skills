---
name: ask-sync-to-claude-skills
description: "After creating a new skill or memory, ask whether to sync it to the claude-skills repo (/Users/minhpham/projects/claude-skills)"
metadata:
  node_type: memory
  type: feedback
  originSessionId: 170d1f98-1921-4827-a26e-612631f8207a
  modified: 2026-10-29T07:19:28.273Z
---

Whenever I create a new skill (in `~/.claude/skills/`) or a new memory, ask the user whether to sync it to their setup repo `/Users/minhpham/projects/claude-skills` (GitHub: MarkPhamm/claude-skills).

**Why:** The user keeps their Claude Code setup in that repo so `install.sh` can restore it on a new machine and copy generic memories into every project. Asked for this on 2026-10-29.

**How to apply:**
- Ask once, right after creating it, in one short line.
- Skill: `cp -R ~/.claude/skills/<name> skills/` and add a row to the "My skills" table in `README.md`.
- Memory: only generic ones (how to write, review, commit), not project-specific facts. Copy into `memory/<category>/` and add its line to `memory/MEMORY.md`.
- Commit there only after the user says yes; push only when asked. See [[ask-base-branch]] and [[no-claude-code-attribution]].
