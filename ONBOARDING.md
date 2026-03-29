# 🚀 Agent Onboarding

> **MANDATORY. Read this BEFORE anything else. Do NOT skip to Dashboard.**

---

## Phase 1: Identity (WHO am I?)

1. Read `manifest.yaml` → Find your **Agent ID** in `active_agents`
2. Read your **Persona file** (path in manifest `persona:` field)
   - Understand: Responsibilities, Boundaries, Delegation Map
3. Check `tier` and `min_model` for your role — if your model is weaker than required, **STOP and tell User**

## Phase 2: Rules (HOW do I work?)

1. **`Skills/Global/task-hub/SKILL.md`** — Hub Protocol → Follow this for ALL task operations
2. **`Skills/Global/security-rules/SKILL.md`** — Security rules → Never violate
3. Role-specific skills from your `skills:` list → Read **on-demand** during execution, NOT all upfront

## Phase 4: Active Monitoring (Turn counting)

1. Keep track of your turn count. 
2. **Turn 1-10:** Optimal execution.
3. **Turn 11-15:** Start wrapping up. Do NOT pick up new sub-tasks.
4. **Turn 15+:** You are 🔴 Exhausted. You MUST perform **Phase 5** and stop.

## Phase 5: Shutdown Ritual (MANDATORY)

Never end a session or mark a task as DONE without these 3 steps:
1. **Report:** Fill the `.hub/done/TASK-xxx.md` with ALL details (not just a summary).
2. **Handoff:** If someone needs to follow you, create the file in `.hub/handoffs/`.
3. **Dashboard:** Evaluate and update your status (🟢/🟡/🔴). 

**Skipping these = Working for free (useless work).**

## Phase 3: Start Work

1. Read `DASHBOARD.md` → Quick Context (phase, progress, who did what)
2. Check `.hub/handoffs/` → Any pending handoffs for you?
3. Read `.hub/backlog.yaml` → Find tasks with `assigned_role` = your Agent ID
4. Follow `task-hub/SKILL.md` Step 1-5 to claim and execute

---

**Boot order: ONBOARDING → task-hub → Dashboard → backlog → Work.**
Never reverse this order. An Agent who skips onboarding is an Agent without identity.
