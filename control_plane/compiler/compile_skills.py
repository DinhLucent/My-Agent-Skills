"""Compile Skills — Parse Skills/**/SKILL.md → skill_index.json.

Extracts tags, triggers, preferred roles, and task types from skill
content so the router knows when to load which skill without reading
every SKILL.md at runtime.
"""
from __future__ import annotations

import json
import re
from pathlib import Path
from typing import Any

import yaml


# Role keywords to detect in skill text
_ROLE_KEYWORDS = ["backend", "frontend", "qa", "reviewer", "security", "docs", "devops"]

# Task type keywords
_TASK_TYPE_KEYWORDS = [
    "bugfix", "feature", "refactor", "documentation", "release", "incident", "test",
]

# Trigger keywords
_TRIGGER_KEYWORDS = [
    "auth", "login", "token", "release", "doc", "bug", "incident",
    "refactor", "test", "deploy", "security", "api", "database",
    "performance", "review", "scan", "audit",
]

# Context type keywords
_CONTEXT_KEYWORDS = ["task_packet", "code", "tests", "handoff", "verification_report"]


def compile_skills(repo_root: Path) -> Path:
    """Walk Skills/ and .skills_pool/ to produce skill_index.json."""
    compiled_dir = repo_root / "knowledge" / "compiled"
    compiled_dir.mkdir(parents=True, exist_ok=True)

    compiled: dict[str, Any] = {}

    # Scan Skills/ (project-level skills)
    skills_root = repo_root / "Skills"
    if skills_root.exists():
        _scan_skill_tree(skills_root, skills_root, repo_root, compiled)

    # Scan .skills_pool/ (external skills)
    pool_root = repo_root / ".skills_pool"
    if pool_root.exists():
        _scan_skill_tree(pool_root, pool_root, repo_root, compiled, prefix=".skills_pool/")

    out_path = compiled_dir / "skill_index.json"
    out_path.write_text(json.dumps(compiled, indent=2, ensure_ascii=False), encoding="utf-8")
    return out_path


def _scan_skill_tree(
    root: Path,
    base: Path,
    repo_root: Path,
    compiled: dict[str, Any],
    prefix: str = "",
) -> None:
    """Recursively find SKILL.md files and compile them."""
    for skill_md in root.rglob("SKILL.md"):
        rel = skill_md.parent.relative_to(base).as_posix()
        skill_key = f"{prefix}{rel}" if prefix else rel
        compiled[skill_key] = _parse_skill(skill_md, repo_root)


def _parse_skill(path: Path, repo_root: Path) -> dict[str, Any]:
    """Extract metadata from a single SKILL.md."""
    text = path.read_text(encoding="utf-8", errors="replace")
    name = path.parent.name

    # Try YAML frontmatter
    frontmatter: dict[str, Any] = {}
    body = text
    fm_match = re.match(r"^---\s*\n(.*?)\n---\s*\n(.*)", text, re.DOTALL)
    if fm_match:
        try:
            frontmatter = yaml.safe_load(fm_match.group(1)) or {}
        except yaml.YAMLError:
            pass
        body = fm_match.group(2)

    # Extract first meaningful paragraph as summary
    lines = [l.strip() for l in body.splitlines() if l.strip() and not l.startswith("#")]
    summary = " ".join(lines[:3])[:300]

    return {
        "path": str(path.relative_to(repo_root)),
        "description": frontmatter.get("description", summary),
        "tags": _extract_tags(name, text),
        "preferred_task_types": _infer_from_keywords(text, _TASK_TYPE_KEYWORDS, default=["bugfix", "feature"]),
        "preferred_roles": _infer_from_keywords(text, _ROLE_KEYWORDS, default=["backend"]),
        "required_context_types": _infer_from_keywords(text, _CONTEXT_KEYWORDS, default=["task_packet", "code"]),
        "triggers": _infer_triggers(name, text),
        "summary": summary,
    }


def _extract_tags(name: str, text: str) -> list[str]:
    """Build tag list from skill name + content keywords."""
    base = name.replace("_", "-").lower().split("-")
    lower = text.lower()
    extra = [
        kw for kw in _TRIGGER_KEYWORDS + ["token", "session", "frontend", "backend", "qa"]
        if kw in lower
    ]
    return sorted(set(base + extra))


def _infer_from_keywords(text: str, keywords: list[str], default: list[str]) -> list[str]:
    lower = text.lower()
    found = [kw for kw in keywords if kw in lower]
    return found or default


def _infer_triggers(name: str, text: str) -> list[str]:
    combined = f"{name.lower()} {text.lower()}"
    return sorted({t for t in _TRIGGER_KEYWORDS if t in combined})


if __name__ == "__main__":
    result = compile_skills(Path(".").resolve())
    print(f"Compiled skill index → {result}")
