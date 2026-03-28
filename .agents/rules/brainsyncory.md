

# Project Memory — MyAgentSkills
> 127 notes | Score threshold: >40

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

## 📝 NOTE: 1 uncommitted file(s) in working tree.\n\n## Project Standards

- convention in OPERATING_RULES.md
- problem-fix in task.md — confirmed 5x
- convention in validate-assets.sh
- Strengthened types Audit
- convention in audit_report.md
- Strengthened types Security
- what-changed in task.md — confirmed 7x
- what-changed in SKILL.md — confirmed 5x

## Recent Decisions

- decision in manifest.yaml
- Optimized Goal — introduces API versioning for backward compatibility

## Learned Patterns

- Always: convention in .gitignore (seen 2x)
- Always: Strengthened types Goal (seen 2x)
- Always: convention in .gitignore (seen 4x)
- Agent generates new migration for every change (squash related changes)
- Agent installs packages without checking if already installed

## Available Tools (ON-DEMAND only)
- `query(q)` — Deep search when stuck
- `find(query)` — Full-text lookup
> Context above IS your context. Do NOT call load() at startup.
