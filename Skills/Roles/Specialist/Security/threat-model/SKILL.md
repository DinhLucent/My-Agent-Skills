# Skill Name: Threat Model

> Description: Socratic risk analysis workflow to be performed before implementing high-risk features.

---

## 🛠️ Metadata
- **Triggers**: "/threat-model", "analyze risk", "security design", "what could go wrong"
- **Category**: Specialist / Security
- **Version**: 1.0.0

## 🎯 Primary Instructions
Run this workflow **BEFORE** writing code for any feature involving payments, authentication, or sensitive user data.

1. **Assets**: Identify the valuable data the feature processes.
2. **Threat Actors**: Determine who might attack the feature.
3. **Attack Vectors**: Hypothesize the methods of attack (e.g., SQLi, Path Traversal).
4. **Mitigations**: Propose "Security by Design" defenses.

## 🏗️ Structure & References
- **Workflow Detail**: [workflow.md](file:///d:/MyProject/LucentDinhCompany/Skills/Roles/Specialist/threat-model/workflow.md)

## 📖 Usage Examples

### Example 1: Before building a login form
**User**: "I'm going to build the new authentication module."
**Agent**: "Before we start coding, let's run a `/threat-model` to secure the design."

---
*Output must be a summary table mapping Risk -> Impact -> Mitigation for user approval.*
