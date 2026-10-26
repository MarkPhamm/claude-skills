#!/usr/bin/env bash
# Restore my Claude Code setup on a new machine.
set -euo pipefail
cd "$(dirname "$0")"

# 1. My own skills
mkdir -p ~/.claude/skills
cp -R skills/. ~/.claude/skills/
echo "Copied skills: $(ls skills | tr '\n' ' ')"

# 2. Global instructions (backs up an existing file first)
if [ -f ~/.claude/CLAUDE.md ] && ! cmp -s CLAUDE.md ~/.claude/CLAUDE.md; then
  cp ~/.claude/CLAUDE.md ~/.claude/CLAUDE.md.bak
  echo "Backed up existing ~/.claude/CLAUDE.md to CLAUDE.md.bak"
fi
cp CLAUDE.md ~/.claude/CLAUDE.md

# 3. Plugins
for m in anthropics/claude-plugins-official latent-spaces/brag ayghri/i-have-adhd pbakaus/impeccable; do
  claude plugin marketplace add "$m" || true
done
for p in superpowers@claude-plugins-official brag@brag i-have-adhd@i-have-adhd; do
  claude plugin install "$p" || true
done

# 4. HyperFrames video skills (third-party, installed from source)
npx -y skills add heygen-com/hyperframes -g -a claude-code -y || echo "HyperFrames install failed; run: npx skills add heygen-com/hyperframes"

echo "Done. Start a new Claude Code session to load everything."
