---
description: "Agent lifecycle for V2 Orchestrator — boot, execute, verify, shutdown"
---

# Agent Lifecycle (V2 Orchestrator)

> This workflow describes how agents operate under the V2 Orchestrator (`run_orchestrator.py`).
> The orchestrator handles task assignment, execution, and verification automatically.

---

## Phase 1: BOOT

The orchestrator loads the agent's identity and skills from `manifest.yaml`:
1. Resolve agent ID and persona from manifest
2. Load role skills and security constraints
3. Build execution context via `control_plane/context_builder/`

**Output:** Agent is initialized with identity, skills, and project context.

---

## Phase 2: TASK ASSIGNMENT

Tasks are assigned via the control plane — **not** via manual `.hub/` claiming:
1. Orchestrator creates a task packet (`templates/task_packet.json` schema)
2. Task is routed to the appropriate agent based on `assigned_role`
3. Agent receives the packet with acceptance criteria and context

---

## Phase 3: EXECUTE

1. Agent executes the task within role boundaries
2. Progress is tracked by `task_state_machine.py`
3. If blocked → orchestrator handles escalation
4. Stress monitoring is handled by the orchestrator, not self-reported

---

## Phase 4: VERIFY

1. Orchestrator runs `verifier/` checks on the output
2. If verification fails → retry loop with feedback
3. If verification passes → task moves to finalized state

---

## Phase 5: FINALIZE & SHUTDOWN

1. Task report is generated automatically
2. Git workflow (commit, branch) is handled per `GIT_WORKFLOW.md`
3. Handoff context is preserved in execution state, not manual `.hub/handoffs/`
4. Session ends cleanly

---

## Files Referenced

| File | Purpose |
|------|---------|
| `manifest.yaml` | Agent registry + skill mapping |
| `control_plane/orchestrator.py` | Main orchestrator loop |
| `control_plane/execution/agent_executor.py` | Task execution engine |
| `control_plane/execution/task_state_machine.py` | State transitions |
| `control_plane/verifier/` | Output verification |
| `templates/task_packet.json` | Task packet schema |
| `templates/verification_report.json` | Verification report schema |
| `OPERATING_RULES.md` | Behavioral rules |
| `GIT_WORKFLOW.md` | Git workflow conventions |
