

# Project Memory — My-Agent-Skills
> 174 notes | Score threshold: >40

## Safety — Never Run Destructive Commands

> Dangerous commands are actively monitored.
> Critical/high risk commands trigger error notifications in real-time.

- **NEVER** run `rm -rf`, `del /s`, `rmdir`, `format`, or any command that deletes files/directories without EXPLICIT user approval.
- **NEVER** run `DROP TABLE`, `DELETE FROM`, `TRUNCATE`, or any destructive database operation.
- **NEVER** run `git push --force`, `git reset --hard`, or any command that rewrites history.
- **NEVER** run `npm publish`, `docker rm`, `terraform destroy`, or any irreversible deployment/infrastructure command.
- **NEVER** pipe remote scripts to shell (`curl | bash`, `wget | sh`).
- **ALWAYS** ask the user before running commands that modify system state, install packages, or make network requests.
- When in doubt, **show the command first** and wait for approval.

**Stack:** Unknown stack

## 📝 NOTE: 1 uncommitted file(s) in working tree.\n\n## Important Warnings

- **gotcha in CHEATSHEET.md** — File updated (external): CHEATSHEET.md

Content summary (233 lines):
#
- **gotcha in manifest.yaml** — -     persona: "Skills/Roles/Architecture/cto.md"
+     tier: 1
-   

## Project Standards

- convention in ONBOARDING.md
- Added session cookies authentication — confirmed 4x
- problem-fix in task.md — confirmed 4x
- Added JWT tokens authentication — prevents XSS injection attacks — confirmed 5x
- Added session cookies authentication — confirmed 6x
- what-changed in task.md — confirmed 3x
- problem-fix in task.md — confirmed 3x
- how-it-works in SKILL.md — confirmed 4x

## Recent Decisions

- decision in DASHBOARD.md

## Verified Best Practices

- Agent generates new migration for every change (squash related changes)
- Agent installs packages without checking if already installed

## Available Tools (ON-DEMAND only)
- `query(q)` — Deep search when stuck
- `find(query)` — Full-text lookup
> Context above IS your context. Do NOT call load() at startup.
