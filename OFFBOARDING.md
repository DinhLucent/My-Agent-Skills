# 🚪 OFFBOARDING — Agent Retirement / Firing Process

> Use this when an Agent is no longer needed for the current Phase (e.g., Code complete, moving to Review) to save tokens and reduce noise.

## 📋 4-Step Checklist (For Agents)

When the CEO requests to offboard an Agent, the system must execute these 4 steps:

- [ ] **1. Clean Backlog (Handoff)**
  - Ensure the departing Agent has NO tasks in `IN_PROGRESS` state (check `.hub/active/` directory).
  - If they do: Write a handoff file in `.hub/handoffs/` or reset the `status` to `todo` in `.hub/backlog.yaml`.

- [ ] **2. Update Manifest**
  - Delete the Agent's ID from the `active_agents` list in `manifest.yaml`.

- [ ] **3. Update Roster (Dashboard)**
  - Remove the Agent's row from the `Active Team (Roles)` table in `DASHBOARD.md`.

- [ ] **4. HR Log Update**
  - Add 1 line to the `HR Log` section in `DASHBOARD.md`.
  - _Format example: `[YYYY-MM-DD] CEO — ACTION: Offboarded [agent-id] (Phase [phase-name] complete)`_

---

## 💡 Guide for CEO

When you see an Agent is idle and want to remove them from the project:

```text
"The project has finished phase X. Please run the OFFBOARDING process for [agent-id] according to OFFBOARDING.md."
```

The system will verify and securely "retire" the Agent. When needed again, you can call the `RECRUITMENT.md` process to "Re-hire" them.
