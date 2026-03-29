# Skill Name: Deep Scan

> Description: A comprehensive security pipeline performing reconnaissance, secret scanning, SAST, and dependency auditing.

---

## 🛠️ Metadata
- **Triggers**: "/deep-scan", "security audit", "scan for vulnerabilities", "check security"
- **Category**: Specialist / Security
- **Version**: 1.0.0

## 🎯 Primary Instructions
When this skill is triggered, you must execute the entire security pipeline defined in the workflow file.

1. **Reconnaissance**: Understand the target architecture and inputs.
2. **Secret Audit**: Search for exposed credentials or tokens.
3. **SAST (Static Analysis)**: Find dangerous code patterns and logic flaws.
4. **Dependency Audit**: Review libraries for known CVEs.
5. **Reporting**: Produce a categorized vulnerability report.

## 🏗️ Structure & References
- **Workflow Detail**: [workflow.md](file:///d:/MyProject/LucentDinhCompany/Skills/Roles/Specialist/deep-scan/workflow.md)

## 📖 Usage Examples

### Example 1: Starting a security review
**User**: "Run a security audit on the `/auth` directory."
**Agent**: "Initiating `/deep-scan`. Starting Phase 1: Reconnaissance..."

---
*Follow Global Security Rules at all times.*
