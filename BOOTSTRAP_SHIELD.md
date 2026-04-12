# BOOTSTRAP_SHIELD

How to apply SHIELD to another repository.

This guide is for the most common case:

- you cloned an existing repo from somewhere else
- you want to improve it, fix issues, or continue development
- you want to use SHIELD without guessing the setup

## Important Rule

With the current architecture, SHIELD should live at the **root of the target repository**.

Do **not** place it under a subfolder like:

```text
my-app/shield/
```

The current CLI uses the folder that contains `run_orchestrator.py` as the repository root.

## Two Adoption Modes

| Mode | Use when | What you use |
|------|----------|--------------|
| Prompt-only | New repo, short engagement, still exploring | `PROMPT_PACK.md`, Prompt Builder, `GENERAL.md` |
| Full runtime | Long-term repo, real execution workflow needed | `control_plane/`, `run_orchestrator.py`, `templates/`, `manifest.yaml` |

If you are unsure, start with **Prompt-only** first.

---

## Path A: Prompt-only Adoption

Use this when:

- you just cloned the repo
- you are still learning the codebase
- you do not want to embed SHIELD runtime yet

### Steps

1. Clone the target repo.
2. Run the target repo locally.
3. Make sure build, start, and tests work.
4. Use `PROMPT_PACK.md` and Prompt Builder to:
   - understand the repo
   - create an improvement plan
   - fix small issues
   - plan the first tasks
5. Write a short `PROJECT_CONTEXT.md` in the target repo.
6. Pick one small real task and finish it.

### Recommended order

1. Understand the repo
2. Write context
3. Validate with a small task
4. Only then decide whether to embed SHIELD runtime

---

## Path B: Full Runtime Adoption

Use this when:

- the repo will be worked on seriously
- you want `compile -> plan -> run -> verify -> retry`
- you want task packets, metrics, and handoff artifacts

## Step 1: Clone The Target Repo

```bash
git clone <target-repo>
cd <target-repo>
git checkout -b shield-bootstrap
```

## Step 2: Copy SHIELD Core Into The Target Repo Root

Copy these directories and files into the **root** of the target repo:

### Required

- `control_plane/`
- `run_orchestrator.py`
- `templates/`
- `manifest.yaml`

### Strongly recommended

- `README.md`
- `CHEATSHEET.md`
- `GENERAL.md`
- `SYSTEM_AUDIT.md`
- `PROMPT_PACK.md`
- `tools/prompt-builder/`

### Optional

- `Skills/`
- `STATUS.md`

### Do not copy by default

- `.skills_pool/`
- `refs_github/`
- `_agent/`
- generated `runtime/`
- generated `knowledge/compiled/`
- generated `.hub/`

---

## Step 3: Add Ignore Rules

Add these to the target repo `.gitignore`:

```gitignore
runtime/state/
runtime/cache/
runtime/sessions/
runtime/reports/
.hub/
knowledge/compiled/
knowledge/memory/
__pycache__/
*.pyc
.env
venv/
```

These are generated or environment-specific artifacts.

---

## Step 4: Install Minimal Dependencies

The current SHIELD runtime needs Python plus `PyYAML`.

```bash
python -m venv .venv
.venv\Scripts\activate
pip install pyyaml
```

Then install the normal dependencies of the target repo itself.

Examples:

- `pytest`
- `ruff`
- `mypy`
- `npm install`
- `eslint`

Those depend on the target repo, not on SHIELD itself.

---

## Step 5: Add Minimal Project Files

### `DASHBOARD.md`

Recommended minimal version:

```md
# DASHBOARD

## TODO
| Task | Title | Role |
|------|-------|------|
```

The dashboard is optional, but having it makes project context easier to carry.

### `manifest.yaml`

Start small.

Do not bring a huge role catalog into a fresh target repo on day one.

Recommended initial roles:

- backend
- frontend
- fullstack
- qa
- security or reviewer

---

## Step 6: Compile

```bash
python run_orchestrator.py compile
```

This should generate:

- `knowledge/compiled/role_index.json`
- `knowledge/compiled/skill_index.json`
- `knowledge/compiled/project_index.json`
- `knowledge/compiled/module_index.json`
- `runtime/cache/summaries/dashboard_snapshot.json`

If compile does not pass, stop and fix bootstrap first.

---

## Step 7: Run A Smoke Task

Create a very small task first.

Example:

```yaml
schema_version: "2.1"
id: TASK-SMOKE-001
title: Create proof file
description: Validate SHIELD execution loop in this repository.
assigned_role: backend
priority: low
status: queued
domain: general

inputs:
  related_paths:
    - README.md
  related_tests: []
  related_handoffs: []
  related_logs: []
  related_modules: []

constraints:
  - minimal_change_only

acceptance_criteria:
  - proof file exists

metadata:
  execution:
    primary_commands:
      - "New-Item -ItemType Directory -Force -Path 'runtime/sessions' | Out-Null"
      - "Set-Content -Path 'runtime/sessions/proof.txt' -Value 'ok' -Encoding utf8"
    output_files:
      - runtime/sessions/proof.txt
    satisfied_criteria:
      - proof file exists
```

Then run:

```bash
python run_orchestrator.py plan path/to/task.yaml
python run_orchestrator.py run path/to/task.yaml
```

---

## Step 8: Use SHIELD For Real Work

Once the smoke task passes, move to a real small task.

Good first tasks:

- fix a typo or bad error message
- add one missing test
- tighten one validation rule
- improve one small log or config issue

For each task:

1. set `inputs.related_paths`
2. write clear `acceptance_criteria`
3. add `metadata.execution.primary_commands`
4. run `plan`
5. run `run`
6. inspect reports

---

## Step 9: Read The Right Outputs

After a run, check:

- `runtime/state/task_packets/`
- `runtime/state/agent_runs/`
- `runtime/state/verification_reports/`
- `runtime/reports/metrics/`
- `.hub/done/`
- `.hub/handoffs/` when a task fails

---

## Step 10: Roll Out Gradually

Do not apply SHIELD to every workflow on day one.

Recommended rollout:

1. smoke task
2. one real small task
3. one retry scenario
4. weekly or release-related tasks
5. broader team adoption

---

## Common Mistakes

| Wrong | Right |
|-------|-------|
| Put SHIELD under a subfolder | Place SHIELD at repo root |
| Embed full runtime before the repo even runs locally | First get the target repo running |
| Use a huge manifest on day one | Start with a small manifest |
| Skip `metadata.execution` | Always give runnable commands |
| Treat SHIELD as magic auto-coding | Treat it as a disciplined control plane |
| Roll out to every task immediately | Start with smoke tasks and small wins |

---

## Recommended Decision Rule

Use this shortcut:

- If you are still understanding the repo: use **Prompt-only**
- If you already know the repo and want repeatable execution: use **Full runtime**

---

## Current Limitation

SHIELD is not yet packaged as:

```bash
pip install shield
```

or:

```bash
python -m shield bootstrap <repo>
```

Right now, the practical model is:

**vendor SHIELD into the target repo root and use it as an internal control plane**
