---
name: issues-finders-and-resolvers
description: End-to-end product improvement loop for a repo. Audit the codebase, UI, docs, CI and anything else the product ships (web app, site, VS Code extension, CLI) to find the 3 to 5 most critical problems. File them as GitHub issues, plan each fix, open one PR per issue, and merge once CI and verification pass. Use whenever the user asks to "find and fix issues", "audit and fix", "find what's broken and fix it", "improve the product end to end", "find issues, file them, resolve them", or wants Claude to go from no known issues to merged fixes, even if they do not name this skill. Prefer it over product-issue-audit (which only files issues) and issues-resolvers (which only works existing issues) when the user wants both halves.
---

# Issues finders and resolvers

The user wants the product better by the end of the session, not a report about it. Find the few problems that hurt users most, write each one up so it stands on its own, fix them in order of severity, and merge the fixes.

Five stages, run in order:

1. **Orient**: learn what the product promises and how the repo works.
2. **Audit**: find candidate problems and confirm each one.
3. **Pick and file**: rank them, keep the top 3 to 5, and file them as issues.
4. **Plan**: write a short fix plan for each issue.
5. **Resolve**: one PR per issue, most critical first, verified, merged.

The user asked for the whole loop, so there is no approval gate between stages. That makes your own verification the only quality gate, and every stage below is built around it. If the user asks to review the issues or plans first, stop at that point and wait.

## 1. Orient

From the repo root:

```bash
gh repo view --json nameWithOwner,defaultBranchRef,url,homepageUrl
gh issue list --state all --limit 100 --json number,title,state,labels
gh pr list --state open --json number,title,headRefName
gh label list
```

Read `README`, `CLAUDE.md`, `CONTRIBUTING.md`, `docs/`, the CI workflows and `package.json` (or the equivalent). You need three things from them:

- **The spec.** What the product says it does. A promised feature that does not work is a bug.
- **The gates.** The exact commands for test, typecheck, lint and integration tests, and any rule such as "screenshot UI before push".
- **The conventions.** Commit subject style, changelog rules, branch naming and merge method. Check `gh pr list --state merged --limit 5` and `git log --oneline -10` to see how PRs usually land.

Also check user memory for standing rules about merging, releasing or confirmation, and follow them.

## 2. Audit

Look at every surface the product ships, weighted by how much users use it. Spend most of the effort on the main flow, from first arrival to first success.

**Run the product.** Start the app, site, extension host or CLI the way the docs say. Use browser tools or Playwright for anything with a UI. Click the primary controls, read the console and network errors, and check phone width and wide width. Check keyboard access, labels and contrast. Check empty, loading and error states. Every UI finding needs a screenshot or a scripted check as evidence.

**Read the code.** Trace each symptom to a file and line. Look for logic errors, unhandled failures, unvalidated input at trust boundaries, race conditions and dead code paths. Check for missing tests on risky logic and for `TODO` or `FIXME` comments that describe real gaps.

**Check the project.** Run the test, typecheck and build commands. Failures here are findings. Do the README install steps still work? Are the docs and screenshots still accurate? Is CI green on the default branch?

**Think about the product.** Improvements count, but only when grounded in something you observed: a dead end in a flow, a gap between two surfaces of the same product, or a promise in the README that the product does not keep. Generic wish-list items that could apply to any repo are noise.

Stay a user, not an attacker. Do not fuzz, inject payloads or hammer live services. If you spot a real security problem, such as a committed secret or an exploitable hole, **do not file it publicly**. Tell the user in chat and point to `SECURITY.md` or GitHub's private vulnerability reporting. Then keep going with the rest.

### Confirm before you count it

A finding counts only when all of these hold:

- **Reproduced twice**, the second time from a clean state (fresh page load, fresh build, new process).
- **Observed, not inferred.** "Clicking Compare logs `TypeError: x is undefined`" is observed. "Probably breaks on Safari" is a guess, so leave it out.
- **Not a duplicate.** Search open and closed issues for its key terms, and check open PRs too.
- **Has a pass/fail check.** You can name a test, command or screenshot that fails now and will pass once fixed. Without one, nobody can tell when the work is done.

## 3. Pick and file

Rank the confirmed findings by severity, then by how many users hit it:

1. Security or data loss, which you report privately as described above and do not file.
2. Crash, broken core flow, or a promised feature that does not work.
3. Wrong output: results that are silently incorrect.
4. Failing build, tests or CI, or broken install or setup steps.
5. UX friction on the main flow, and accessibility failures.
6. Docs drift, polish, and grounded improvements.

Keep the top 3 to 5. Each one must be fixable in one focused PR this session. If the most critical finding is too big for that, or needs a product decision, file it anyway, mark it in the report as "filed, not fixed", and resolve the next ones. Leftover findings go in the final report, not in issues. Five solid issues beat fifteen thin ones.

File each issue with `gh issue create`, applying existing labels only. Use the repo's issue templates if it has any. Otherwise use this:

```markdown
## What happens
One or two plain sentences.

## Steps to reproduce
1. ...

## Expected
## Actual

## Where
File and line as a permalink to a commit SHA, plus the page URL or command.

## Evidence
Error text, failing command output, screenshot.

## Severity
Its rank from the list above and who it affects.
```

For an improvement, use **Problem / Proposal / Why it is worth it** instead.

Titles name the specific problem, for example "Compare button does nothing when the right editor is empty", not "Compare issues". Record each issue's number and URL.

## 4. Plan

Write one plan per issue in chat. It is the contract for the PR.

```
### #N <title>
- Cause: <file:line and what is wrong there>
- Fix: <what changes, 1-3 lines, at the root cause, not one call site>
- Verify: <the check that fails now and passes after, plus the repo's gates>
- Time: <concrete estimate, e.g. "20 min">
```

Use one PR per issue, so each can be reviewed and reverted on its own. Merge two issues into one PR only when they are the same bug seen twice.

## 5. Resolve

Work most critical first, one PR at a time. Branch each one from the freshly updated base, so later PRs do not conflict with earlier merges.

1. `git switch <base> && git pull && git switch -c <branch>`, following the repo's naming convention.
2. Write the regression test or check first, and watch it fail.
3. Fix the root cause. Grep every caller of what you change and update the tests and fixtures it breaks.
4. Run the plan's check and every repo gate from stage 1. For UI changes, take a real screenshot. Fix what breaks.
5. Commit in the repo's style. Add a changelog line if the repo wants one for user-facing changes. Push.
6. Run `gh pr create`. The body says `Fixes #N`, the cause, the fix, and the decisive verification output.
7. Run `gh pr checks <pr> --watch`. If a check fails, read the logs, fix it and push again. Re-run a flaky failure, such as a timeout or a runner dying, once.
8. When CI is green and verification passed, merge with the repo's usual method, for example `gh pr merge <pr> --merge`. Never bypass branch protection or required reviews: no `--admin`. If a review is required, leave the PR open and say so.

Stop and tell the user, rather than shipping something different, if a fix turns out to have a different cause or to be much bigger than planned. Approval to fix the planned problem is not approval to rewrite something else.

Never add AI attribution to commits, PRs or issues: no `Co-Authored-By` trailer, and no "Generated with" line.

## Final report

```
Filed: <n> issues | Merged: <k> PRs
1. #N <title> [severity] -> PR <url> | verified: <decisive output> | merged
2. #N <title> [severity] -> filed, not fixed: <reason>
Left out: <finding> (<reason: duplicate / not reproduced / too minor>)
Private: <security findings, or "none">
Not covered: <surfaces you could not reach, e.g. needs login or real credentials>
```

End with the one next action for the user.
