"""Build Indexes — Master builder that runs all compilers + module index.

Generates:
  - role_index.json
  - skill_index.json
  - project_index.json + context_fragments/
  - module_index.json
  - build_manifest.json
"""
from __future__ import annotations

import json
import sys
from datetime import datetime, timezone
from pathlib import Path
from typing import Any

from control_plane.compiler.compile_roles import compile_roles
from control_plane.compiler.compile_skills import compile_skills
from control_plane.compiler.compile_docs import compile_docs


# ── Module index builder ─────────────────────────────────────

DEFAULT_SOURCE_DIRS = ("src", "app", "services", "packages", "lib")
DEFAULT_TEST_DIRS = ("tests", "test")


def build_module_index(repo_root: Path) -> Path:
    """Scan source/test directories to produce module_index.json."""
    compiled_dir = repo_root / "knowledge" / "compiled"
    fragments_dir = compiled_dir / "context_fragments"
    compiled_dir.mkdir(parents=True, exist_ok=True)
    fragments_dir.mkdir(parents=True, exist_ok=True)

    modules: dict[str, Any] = {}

    source_roots = [repo_root / d for d in DEFAULT_SOURCE_DIRS if (repo_root / d).exists()]
    test_roots = [repo_root / d for d in DEFAULT_TEST_DIRS if (repo_root / d).exists()]

    for source_root in source_roots:
        for child in source_root.iterdir():
            if not child.is_dir():
                continue

            module_name = child.name
            module_paths = [str(child.relative_to(repo_root))]
            related_tests = _find_related_tests(repo_root, module_name, test_roots)
            entrypoints = _find_entrypoints(repo_root, child)
            summary_fragment = fragments_dir / f"{module_name}.summary.json"

            # Create placeholder fragment if none exists
            if not summary_fragment.exists():
                summary_fragment.write_text(
                    json.dumps({
                        "module": module_name,
                        "summary": f"Auto-generated summary placeholder for {module_name}.",
                        "paths": module_paths,
                        "entrypoints": entrypoints,
                        "related_tests": related_tests,
                    }, indent=2, ensure_ascii=False),
                    encoding="utf-8",
                )

            modules[module_name] = {
                "paths": module_paths,
                "owners": _infer_owners(module_name),
                "entrypoints": entrypoints,
                "related_tests": related_tests,
                "dependencies": [],
                "risk_level": _infer_risk(module_name),
                "summary_fragment": str(summary_fragment.relative_to(repo_root)),
            }

    out_path = compiled_dir / "module_index.json"
    out_path.write_text(json.dumps(modules, indent=2, ensure_ascii=False), encoding="utf-8")
    return out_path


def _find_related_tests(repo_root: Path, module_name: str, test_roots: list[Path]) -> list[str]:
    matches: list[str] = []
    for test_root in test_roots:
        for path in test_root.rglob("*"):
            if path.is_file() and module_name in path.as_posix():
                matches.append(str(path.relative_to(repo_root)))
    return sorted(set(matches))


def _find_entrypoints(repo_root: Path, module_dir: Path) -> list[str]:
    candidates: list[str] = []
    for path in module_dir.rglob("*.py"):
        name = path.name.lower()
        if name in {"main.py", "__init__.py"} or any(
            kw in name for kw in ("service", "controller", "api", "router", "handler")
        ):
            candidates.append(str(path.relative_to(repo_root)))
    return sorted(set(candidates))[:10]


def _infer_owners(module_name: str) -> list[str]:
    sensitive = {"auth", "billing", "payments", "security", "admin"}
    if module_name in sensitive:
        return ["backend", "qa", "security"]
    return ["backend", "qa"]


def _infer_risk(module_name: str) -> str:
    high = {"auth", "billing", "payments", "security", "admin"}
    return "high" if module_name in high else "medium"


# ── Master builder ───────────────────────────────────────────

def build_all(repo_root: Path) -> dict[str, str]:
    """Run every compiler and return a manifest of generated files."""
    print("=" * 60)
    print("  Agents-of-SHIELD — Knowledge Compiler v2")
    print("=" * 60)

    results: dict[str, str] = {}

    # 1. Roles
    print("\n[1/4] Compiling roles from manifest.yaml ...")
    try:
        role_path = compile_roles(repo_root)
        results["role_index"] = str(role_path)
        print(f"  ✓ {role_path}")
    except Exception as e:
        print(f"  ✗ Failed: {e}")

    # 2. Skills
    print("\n[2/4] Compiling skills from Skills/ ...")
    try:
        skill_path = compile_skills(repo_root)
        results["skill_index"] = str(skill_path)
        print(f"  ✓ {skill_path}")
    except Exception as e:
        print(f"  ✗ Failed: {e}")

    # 3. Docs
    print("\n[3/4] Compiling docs ...")
    try:
        doc_paths = compile_docs(repo_root)
        for p in doc_paths:
            results[p.stem] = str(p)
            print(f"  ✓ {p}")
    except Exception as e:
        print(f"  ✗ Failed: {e}")

    # 4. Module index
    print("\n[4/4] Building module index ...")
    try:
        module_path = build_module_index(repo_root)
        results["module_index"] = str(module_path)
        print(f"  ✓ {module_path}")
    except Exception as e:
        print(f"  ✗ Failed: {e}")

    # Write build manifest
    manifest = {
        "built_at": datetime.now(timezone.utc).isoformat(),
        "repo_root": str(repo_root),
        "compiler_version": "2.0",
        "outputs": results,
    }
    manifest_path = repo_root / "knowledge" / "compiled" / "build_manifest.json"
    manifest_path.write_text(json.dumps(manifest, indent=2, ensure_ascii=False), encoding="utf-8")

    print(f"\n{'=' * 60}")
    print(f"  Build complete: {len(results)} artifacts")
    print(f"  Manifest: {manifest_path}")
    print(f"{'=' * 60}")

    return results


if __name__ == "__main__":
    root = Path(sys.argv[1]).resolve() if len(sys.argv) > 1 else Path(".").resolve()
    build_all(root)
