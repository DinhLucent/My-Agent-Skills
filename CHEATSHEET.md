# 📋 CHEATSHEET — Quick Reference for CEO

> Open this file when you don't know what to do. Find your situation → follow the action.

---

## 🚀 Starting a New Project

| Step | You Do | Which Agent |
|------|--------|-------------|
| 1 | Describe project (tech stack, requirements, scale) | → `producer-agent` or `cto-agent` |
| 2 | AI suggests team → You approve | → AI updates `active_agents` |
| 3 | AI runs `/sprint-plan` → Tasks go to Hub | → You review sprint plan |
| 4 | Open session for each Agent → They grab tasks | → You review each output |

---

## 🔧 Common Situations

| Situation | Open Agent | Action |
|-----------|------------|--------|
| **New Project** | `producer-agent` | Describe project → AI analyzes → suggests team → sprint plan |
| **New Feature** | `producer-agent` | Describe feature → AI splits tasks → assigns roles → to Hub |
| **Bug Report** | `qa-lead-agent` | Describe bug → AI creates prioritized task + assigns role |
| **Urgent Hotfix** | `security-agent` → `backend-agent` | Assess → Fix → Review → Deploy |
| **Scope Change** | `cto-agent` | Describe change → AI assesses impact → plans |
| **New Sprint** | `producer-agent` | `/sprint-plan` → New tasks to Hub |
| **Release** | `release-manager-agent` | `/release-checklist` → deploy → monitor |
| **Missing Role** | AI reports automatically → Open new session | Hire new Agent per `RECRUITMENT.md` |
| **Task Done (Fire)** | `producer-agent` | "Run OFFBOARDING for [agent-id]" |
| **Code Review** | `lead-programmer-agent` | `/code-review` |
| **Security Audit** | `security-agent` | `/deep-scan` |
| **Performance Issue**| `performance-analyst-agent` | `/perf-profile` |
| **UI/UX Feedback** | `ux-designer-agent` | Describe issue → AI suggests fix |
| **Retrospective** | `producer-agent` | `/retrospective` at end of sprint |

---

## 🤔 Don't know which Agent to open?

```
→ Open producer-agent. It will sort and orchestrate for you.
```

---

## 📝 What to say in each session?

### First time (new project):
```
"I want to build [project description].
 Tech: [stack].
 Special requirements: [high security / real-time / mobile-first / ...]
 Scale: [small / medium / large]"
```

### Subsequent sessions (Agent Hub is active):
```
"Pick up task from Hub and execute"
```
→ Agent reads Dashboard + backlog + handoffs → works automatically.

### When a new issue arises:
```
"Issue: [description]. Create a task in the Hub."
```

---

## 🔄 Daily Workflow

```
Morning: Open DASHBOARD.md → Check overall progress
         Producer: "Sprint status?"
       
Work:    Open Agent based on task → Grabs task from Hub
         Review output → Approve / request changes
       
End:     Check DASHBOARD.md → See completed tasks today
         Found issue? → Create new task in Hub
```

---

## ⚡ Frequently Used Slash Commands

| Command | When to use |
|---------|-------------|
| `/brainstorm` | New ideas, unclear concepts |
| `/sprint-plan` | Sprint planning, creating tasks |
| `/code-review` | Code review before merge |
| `/deep-scan` | Security check |
| `/gate-check` | Ready to switch phases? |
| `/release-checklist` | Prep for release |
| `/retrospective` | End of sprint, lessons learned |

---

## 📊 Checking Progress

Open `DASHBOARD.md` → View:
- **Quick Context** → Current Phase, % complete
- **Task Board** → Who is doing what
- **Timeline** → Recent history

---

## ⚠️ Core Rules to Remember

1. **Describe, Don't Dictate** → Let AI suggest approach, you approve
2. **1 Agent 1 Session** → Don't mix roles in one session
3. **Always Review** → AI finishes → you approve → move on
4. **Hub is the Center** → All tasks go through Hub, no side work
