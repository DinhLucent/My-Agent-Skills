# Skill Name: Self-Evolution

> Description: Enables agents to analyze their task performance, update their own skills, and document lessons learned.

---

## 🛠️ Metadata
- **Triggers**: "/auto-reflect", "optimize yourself", "learn from this", "complex bug fixed"
- **Category**: Global / Meta-Cognition
- **Version**: 1.0.0

## 🎯 Primary Instructions
When this skill is triggered, you must execute the **Self-Evolution Loop** to ensure continuous improvement.

1. **Analysis**: Review the last 10 task steps for patterns or recurring errors.
2. **Standardization**: Create new workflows in `GeneralSkills/.agents/workflows/` for successful command sequences.
3. **Refinement**: Self-correct errors in existing `SKILL.md` files if tools or patterns have changed.
4. **Knowledge Persistence**: Document lessons in `tasks/lessons.md`.

## 🏗️ Structure & References
- **Workflow**: [auto-reflect.md](file:///d:/MyProject/LucentDinhCompany/Skills/Global/Evolution/auto-reflect.md)
- **Lessons Log**: [lessons.md](file:///d:/MyProject/LucentDinhCompany/tasks/lessons.md)

## 📖 Usage Examples

### Example 1: After solving a complex setup
**Agent**: "I have successfully configured the multi-agent pipeline. I will now run `/auto-reflect` to capture this workflow for future use."

---
*Generated using LucentDinhCompany Workflow*
