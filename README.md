# claude-skills

My Claude Code skills and setup.

## Install on a new computer

```
git clone https://github.com/MarkPhamm/claude-skills.git
cd claude-skills
./install.sh
```

Needs Node 20+ for the HyperFrames step (`node -v` to check).

Then open a new Claude Code session and type `/tldr` to check.

## What's inside

- `skills/` — my own skills (copied to `~/.claude/skills/`)
- `CLAUDE.md` — global instructions (copied to `~/.claude/CLAUDE.md`)
- `install.sh` — also installs plugins (superpowers, brag, i-have-adhd, caveman, ponytail) and the HyperFrames skills

## Add a new skill

```
cp -R ~/.claude/skills/<name> skills/
git add skills/<name> && git commit -m "Add <name> skill" && git push
```
