# claude-skills

My Claude Code setup: my own skills, global instructions, and one script that installs every plugin and skill pack I use.

## Install on a new computer

```
git clone https://github.com/MarkPhamm/claude-skills.git
cd claude-skills
./install.sh
```

Then open a new Claude Code session and type `/tldr` to check.

**Requirements**

| Tool | Needed for | Check |
|---|---|---|
| [Claude Code](https://claude.com/claude-code) | everything | `claude --version` |
| Node 20+ (22+ for taste-skill) | HyperFrames, Emil Kowalski skills, taste-skill | `node -v` |
| [uv](https://docs.astral.sh/uv/) | Graphify | `uv --version` |
| Python 3.10+ | Graphify, logo-design scripts | `python3 --version` |
| Chrome / Chromium | taste-skill browser check | — |

If a step fails, fix the requirement and run `./install.sh` again. Running it twice is safe.

## What's inside

| Path | What it is | Installed to |
|---|---|---|
| `skills/` | My own skills | `~/.claude/skills/` |
| `CLAUDE.md` | Global instructions (no AI attribution in commits or PRs) | `~/.claude/CLAUDE.md` (existing file backed up as `CLAUDE.md.bak`) |
| `install.sh` | Installs everything below | — |

## My skills

| Skill | What it does |
|---|---|
| [`tldr`](skills/tldr/SKILL.md) | `/tldr` summarises a conversation, file, PR, branch, URL or log in 80 words max: bottom line, up to 3 bullets, next action |

## Plugins

| Plugin | Source | What it does |
|---|---|---|
| superpowers | [anthropics/claude-plugins-official](https://github.com/anthropics/claude-plugins-official) | Workflow skills: brainstorming, plans, TDD, systematic debugging, code review |
| code-review | [anthropics/claude-plugins-official](https://github.com/anthropics/claude-plugins-official) | Reviews a pull request |
| mattpocock-skills | [mattpocock/skills](https://github.com/mattpocock/skills) | Engineering skills: `/tdd`, `/grill-me`, `/to-spec`, `/triage`, `/pr`, `/diagnosing-bugs`. Run `/setup-matt-pocock-skills` once per repo |
| example-skills | [anthropics/skills](https://github.com/anthropics/skills) | Anthropic's example skills: skill creator, frontend design, canvas art, MCP builder |
| andrej-karpathy-skills | [multica-ai/andrej-karpathy-skills](https://github.com/multica-ai/andrej-karpathy-skills) | Coding guidelines based on Karpathy's notes on LLM coding pitfalls |
| ponytail | [DietrichGebert/ponytail](https://github.com/DietrichGebert/ponytail) | Pushes toward the smallest change that solves the task; `/ponytail-review`, `/ponytail-audit` |
| caveman | [JuliusBrussee/caveman](https://github.com/JuliusBrussee/caveman) | Terse replies to cut output tokens; `/caveman`, `/caveman-review`, `/caveman-commit` |
| i-have-adhd | [ayghri/i-have-adhd](https://github.com/ayghri/i-have-adhd) | Replies lead with the next action, numbered steps, short lists |
| taste-skill | [leonxlnx/taste-skill](https://github.com/leonxlnx/taste-skill) | Art direction, reference images and a browser check for frontend pages |
| logo-design | [kaankiziltug/logo-design-skill](https://github.com/kaankiziltug/logo-design-skill) | Logo design from brief to SVG to brand guidelines, with a 1,400+ logo reference library |
| brag | [latent-spaces/brag](https://github.com/latent-spaces/brag) | `/brag` turns a project website into a short launch video |

## Skill packs

Installed with [`npx skills`](https://skills.sh) or their own CLI, not as plugins.

| Pack | Source | Skills |
|---|---|---|
| HyperFrames (21 skills) | [heygen-com/hyperframes](https://github.com/heygen-com/hyperframes) | Video and motion graphics: `hyperframes`, `embedded-captions`, `faceless-explainer`, `motion-graphics`, `product-launch-video`, `slideshow`, `media-use` and more |
| Emil Kowalski (15 skills) | [emilkowalski/skills](https://github.com/emilkowalski/skills) | UI and animation: `animate`, `animate-expo`, `improve-animations`, `review-animations`, `apple-design`, `mobile-native`, `break-ui`, `prototype`, `write-swift` and more |
| Graphify | [Graphify-Labs/graphify](https://github.com/Graphify-Labs/graphify) | `/graphify .` turns a codebase into a queryable knowledge graph. Installed with `uv tool install graphifyy` (double y) |

## Not in this repo

These arrive on their own and need no install:

- **claude.ai skills** (`docx`, `pdf`, `pptx`, `xlsx`, `morning`, `skill-creator` …) sync when you log in to Claude Code.
- **Built-in skills** (`/code-review`, `/simplify`, `/loop`, `claude-api` …) ship with Claude Code.

## Overlaps to know about

- **Reply style:** caveman and i-have-adhd both control how Claude writes. Disable one if replies look clipped: `claude plugin disable caveman@caveman`.
- **Code review:** built-in `/code-review`, the code-review plugin, `/ponytail-review`, `/caveman-review` and Matt Pocock's `code-review` all trigger on "review this".
- **`prototype`:** both Emil Kowalski's pack and mattpocock-skills have one.

## Add something new

**Your own skill:**

```
cp -R ~/.claude/skills/<name> skills/
git add skills/<name> && git commit -m "Add <name> skill" && git push
```

**A plugin:** add its GitHub repo to the `for m in …` line and `<plugin>@<marketplace>` to the `for p in …` line in `install.sh`, then add a row to the table above.
