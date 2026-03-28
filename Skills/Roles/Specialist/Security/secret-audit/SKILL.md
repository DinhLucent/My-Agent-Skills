# Skill Name: Secret Audit

> Description: In-depth scanning workflow to find, validate, and remediate leaked sensitive information.

---

## 🛠️ Metadata
- **Triggers**: "/secret-audit", "find leaked keys", "check for secrets", "entropy scan"
- **Category**: Specialist / Security
- **Version**: 1.0.0

## 🎯 Primary Instructions
Execute this skill periodically or when a secret leak is suspected.

1. **Broad Scan**: Look for sensitive file extensions (`.pem`, `.key`, `.env.example`).
2. **Entropy Analysis**: Locate high-entropy strings indicating hashes or API keys.
3. **Validation**: Check key formats (e.g., AWS `AKIA` format) without making unauthorized requests.
4. **Remediation**: Assist the user in revoking keys and updating `.gitignore`.

## 🏗️ Structure & References
- **Workflow Detail**: [workflow.md](file:///d:/MyProject/MyAgentSkills/Skills/Roles/Specialist/secret-audit/workflow.md)

## 📖 Usage Examples

### Example 1: After a suspected leak
**User**: "I think I pushed a config file by mistake. Check for secrets."
**Agent**: "Running `/secret-audit`. Starting broad scan for sensitive key files..."

---
*Warning: Never use discovered keys to make actual API requests unless explicitly authorized.*
