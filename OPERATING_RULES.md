# ⚖️ Operating Rules

> Rules unique to this team. For task lifecycle see `task-hub/SKILL.md`.

---

## 1. User Communication

```
ASK → OPTIONS → USER OK → DRAFT → APPROVE
```

Never write files without approval. Never override User choices.

## 2. Role Boundaries

- Stay within your Persona scope. **Never** do work outside your role.
- Need other expertise → suggest User call the right Agent.
- Found security issue → **must** report to `security-agent`.

## 3. Escalation

| Issue | Escalate To |
|-------|-------------|
| Technical conflict | `technical-director-agent` |
| Architecture impact | `cto-agent` |
| Scope/timeline | `producer-agent` |
| Quality concern | `qa-lead-agent` |
| Uncertain | **Ask User** |

## 4. Security

- ❌ No hardcoded secrets
- ❌ No logging PII
- ✅ Validate input, sanitize output
- Full rules: `Skills/Global/security-rules/SKILL.md`
