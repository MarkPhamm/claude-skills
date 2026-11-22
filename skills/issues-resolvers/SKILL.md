---
name: issues-resolvers
description: Triage a repo's open GitHub issues, pick the ones worth fixing now, propose a fix plan per issue (solution, how to verify, how many PRs, time estimate), then implement the approved ones as PRs. Use whenever the user asks to "check the issues", "resolve/fix/work through open issues", "go through the backlog", "what issues should we fix", "clear the GitHub issues", or wants Claude to pick and fix bugs from the issue tracker, even if they do not say "skill" or name a specific issue.
---

# Issues resolvers

Two phases with one gate between them:

1. **Plan**: read the open issues, pick the ones worth fixing, and write a plan per issue.
2. **Gate**: the user picks which plans to run.
3. **Do**: implement each approved plan as a PR and verify it.

The gate exists because PRs are outward-facing and the user knows priorities you cannot see. Never skip it, unless the user already said "just do all of them" in this conversation.

## Phase 1: Plan

### 1. Collect

Run these from the repo root:

```bash
gh repo view --json nameWithOwner,defaultBranchRef
gh issue list --state open --limit 100 --json number,title,labels,assignees,createdAt,updatedAt,url,body
gh pr list --state open --limit 100 --json number,title,body,headRefName
```

If the user named issues, a label or a milestone, filter to those. Read the repo's `CLAUDE.md` / `CONTRIBUTING.md` / CI config now: they say how to test, lint and release, and you need that for the verification plan.

### 2. Triage

Skip an issue when any of these hold. Say which rule removed it.

- An open PR already references it (`#N`, "Fixes #N" in a PR body or title).
- It is assigned to someone other than the user.
- It needs a product or design decision the issue does not settle (open-ended feature requests, "should we...?").
- It is too vague to know when it is done, and the comments do not fix that.
- It is labelled `wontfix`, `blocked`, `question`, `duplicate` or similar.

For each remaining issue, read it with comments (`gh issue view N --comments`) and **check the claim against the code** before planning. Open the files it points at. Reproduce the bug when that is cheap (one command, one test, one build). Issues are often wrong about the cause, sometimes already fixed. A plan built on an unchecked issue text is a guess.

Rank: user-facing breakage first (crashes, broken pages, wrong output), then security, then docs/polish.

### 3. Write the plan

Use this template for each picked issue. Keep each field short: the user reads it to decide, not to learn the codebase.

```
### #N <title>
- Problem: <one line, in your words, after checking the code>
- Cause: <file:line and what is wrong there; "confirmed" or "not reproduced">
- Fix: <what changes, 1-3 lines>
- Verify: <exact commands or steps, and what output proves it works>
- PRs: <count, and which issues share a PR>
- Time: <concrete estimate, e.g. "20 min", "half a day">
```

PR count rules:

- Issues whose fix touches the same code, or that are one bug seen twice: one PR.
- Unrelated issues: one PR each, so each can be reviewed and reverted alone.
- One issue that is really several changes: split, and say why.

Verification must be something that fails before the fix and passes after: a new regression test, a command whose output changes, a page that renders. "Run the tests" alone is not a verification plan, because the old suite passed while the bug existed. UI fixes need a real browser check (screenshot or scripted check).

After the plans, list the skipped issues in one line each with the reason, then a total: N issues, M PRs, total time.

## Gate

Ask which plans to run (all, a subset, or changes to a plan). Also ask the base branch if the repo or user memory does not settle it. Wait for the answer.

## Phase 2: Do

Work through the approved PRs one at a time. For each:

1. Branch off the up-to-date base: `git switch <base> && git pull && git switch -c fix/<issue-number>-<slug>`.
2. Write the regression test or check first, and see it fail.
3. Fix the root cause in the shared code, not the symptom at one call site. Grep every caller of what you change.
4. Run the verification from the plan, then the project's full test and lint commands (from step 1). Fix what breaks.
5. Commit with a message that says what changed and why. Push.
6. Open the PR: `gh pr create --base <base> --title ... --body ...`. The body has `Fixes #N` for each issue, the cause, the fix, and how it was verified (paste the decisive output line).
7. If CI runs on PRs, wait for it (`gh pr checks --watch`) and fix failures before moving on.

Do not merge, release or close issues by hand unless the user or the project's instructions say to. If they do (for example a memory saying "merge and release after testing"), follow that.

Never add AI attribution to commits or PRs (no `Co-Authored-By`, no "Generated with" lines).

If the plan turns out wrong mid-fix (different cause, much bigger change), stop that PR and tell the user with the new facts instead of shipping a different fix than the one they approved.

## Final report

One block, short:

```
Done: <k> of <n> PRs
- #N <title> -> <PR url> | verified: <decisive output> | CI: <pass/fail/none>
Not done: <issue, reason>
```

End with the one next action for the user (usually: review PR <url>).
