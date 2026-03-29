# 📋 Agent Recruitment Guide

> Guide for selecting the right Agent for the right role, based on each AI's strengths.

---

## Principle: Right Person — Right Job

Each AI model has different strengths. Wrong model = wasted tokens + poor output.

### Agent Classification by Capability

| Tier | Suitable Roles | Required Capabilities | Recommended Models |
|------|---------------|----------------------|-------------------|
| **Tier 1 — Leadership** | CTO, Technical Director, Producer | Strategic thinking, trade-off analysis, complex decisions | Claude Opus / GPT-4o / Gemini Pro |
| **Tier 2 — Department Lead** | Lead Programmer, PM, QA Lead, UX Designer | Deep analysis, quality review, technical documentation | Claude Sonnet / GPT-4o-mini |
| **Tier 3 — Specialist** | Backend, Frontend, Security, DevOps | Code execution, vulnerability scanning, pipeline ops | Claude Sonnet / Gemini Flash / Haiku |
| **Tier 4 — Executor** | QA Tester, Community Manager, Data Entry | Repetitive tasks, output formatting, batch processing | Haiku / Gemini Flash / GPT-4o-mini |

---

## 5-Step Process: Hiring a New Agent

### Step 1: Identify Need
Answer 3 questions:
- **What's the specific job?** (e.g., "Need AI to review database schema")
- **Complexity level?** → Strategic (Tier 1) or Execution (Tier 3-4)?
- **Which department?** → Architecture | Development | Quality | Management | Specialist

### Step 2: Check Existing Staff
Open `manifest.yaml` → Check if a suitable Agent already exists.
- **Already exists?** → Assign additional skills to that Agent.
- **Doesn't exist?** → Continue to Step 3.

### Step 3: Create Persona for New Agent

```bash
cp templates/SKILL_TEMPLATE.md Skills/Roles/<Department>/<agent-name>.md
```

Persona **MUST** include:
- **Description**: What this Agent does, when to call it.
- **Key Responsibilities**: 3-5 specific responsibilities.
- **Decision Framework**: Criteria the Agent uses for decisions.
- **What This Agent Must NOT Do**: Clear boundaries.
- **Delegation Map**: Who to collaborate with, report to, hand off to.

### Step 4: Assign Skills
Check existing skill inventory:

```
Skills/Global/         → Global skills (all Agents need)
Skills/Roles/          → Specialized skills by department
```

- **Skill exists?** → Assign directly in manifest.
- **Skill missing?** → Create new one using `templates/` workflow.

### Step 5: Register in Manifest

```yaml
# Add to manifest.yaml
  - id: "dba-agent"
    name: "Database Administrator"
    persona: "Skills/Roles/Specialist/Data/dba.md"
    skills:
      - "Skills/Roles/Development/db-review"
      - "Skills/Roles/Quality/perf-profile"
```

---

## Recruitment Confirmation Checklist

- [ ] Persona file created with all 5 mandatory sections
- [ ] Skills assigned (from existing inventory or newly created)
- [ ] Entry added to `manifest.yaml`
- [ ] Tier determined (appropriate model selected)

✅ New Agent ready for onboarding!
