"""On Verification Fail Hook — Produces retry packets with minimal context.

Instead of reloading the entire context, reads the verification report
and augments the original packet with ONLY the failure-specific details.
"""
from __future__ import annotations

import json
from pathlib import Path
from typing import Any


MAX_RETRIES = 3


def on_verification_fail(
    repo_root: Path,
    task_packet_path: Path,
    verification_report_path: Path,
    attempt: int = 1,
) -> dict[str, Any]:
    """
    Read failed verification report and produce a retry packet with only
    minimal additional context. Returns retry info dict.
    """
    packet = json.loads(task_packet_path.read_text(encoding="utf-8"))
    report = json.loads(verification_report_path.read_text(encoding="utf-8"))

    failed_checks = [
        c for c in report.get("checks", []) if c.get("result") == "failed"
    ]
    next_context_needs = report.get("next_context_needs", [])

    # Build retry packet — augment, don't replace
    retry_packet = dict(packet)
    retry_packet["retry_of"] = packet["task_id"]
    retry_packet["retry_attempt"] = attempt
    retry_packet["failure_context"] = {
        "checks": report.get("checks", []),
        "next_context_needs": next_context_needs,
        "failed_check_names": [c["name"] for c in failed_checks],
    }

    # Augment fragments with failure-specific context
    retry_packet["context_fragments"] = _augment_fragments(
        repo_root=repo_root,
        fragments=packet.get("context_fragments", []),
        next_context_needs=next_context_needs,
    )

    retry_packet["verification_plan"] = packet.get("verification_plan", [])
    retry_packet["expected_outputs"] = ["patch", "change_summary", "handoff_update"]

    # Save retry packet
    retry_dir = repo_root / "runtime" / "state" / "task_packets"
    retry_dir.mkdir(parents=True, exist_ok=True)
    out_path = retry_dir / f"{packet['task_id']}.retry-{attempt}.json"
    out_path.write_text(json.dumps(retry_packet, indent=2, ensure_ascii=False), encoding="utf-8")

    should_retry = attempt < MAX_RETRIES

    return {
        "hook": "on_verification_fail",
        "retry_packet_path": str(out_path),
        "failed_checks": [c["name"] for c in failed_checks],
        "additional_context_needed": next_context_needs,
        "attempt": attempt,
        "should_retry": should_retry,
        "should_escalate": not should_retry,
        "escalation_target": "reviewer" if not should_retry else None,
    }


def _augment_fragments(
    repo_root: Path,
    fragments: list[dict[str, Any]],
    next_context_needs: list[str],
) -> list[dict[str, Any]]:
    """Add only the fragments needed for this specific failure."""
    updated = list(fragments)

    for need in next_context_needs:
        fragment = _map_need_to_fragment(repo_root, need)
        if fragment and not any(
            existing.get("id") == fragment["id"] for existing in updated
        ):
            updated.append(fragment)

    return updated


def _map_need_to_fragment(repo_root: Path, need: str) -> dict[str, Any] | None:
    """Map a context need to a concrete fragment reference."""
    cache_dir = repo_root / "runtime" / "cache" / "summaries"
    cache_dir.mkdir(parents=True, exist_ok=True)

    # Known need → fragment mappings
    mapping: dict[str, dict[str, Any]] = {
        "stack_trace": {
            "id": "latest_stack_trace",
            "type": "failure_trace",
            "path": str((cache_dir / "latest_stack_trace.json").relative_to(repo_root)),
        },
        "recent_auth_diff": {
            "id": "recent_auth_diff",
            "type": "recent_diff",
            "path": str((cache_dir / "recent_auth_diff.json").relative_to(repo_root)),
        },
        "token_rotation_helper": {
            "id": "token_rotation_helper",
            "type": "code_hint",
            "path": str((cache_dir / "token_rotation_helper.json").relative_to(repo_root)),
        },
        "failing_test_source": {
            "id": "failing_test_source",
            "type": "test_source",
            "path": str((cache_dir / "failing_test_source.json").relative_to(repo_root)),
        },
        "lint_error_details": {
            "id": "lint_error_details",
            "type": "lint_report",
            "path": str((cache_dir / "lint_error_details.json").relative_to(repo_root)),
        },
        "type_error_details": {
            "id": "type_error_details",
            "type": "typecheck_report",
            "path": str((cache_dir / "type_error_details.json").relative_to(repo_root)),
        },
        "security_finding_details": {
            "id": "security_finding_details",
            "type": "security_report",
            "path": str((cache_dir / "security_finding_details.json").relative_to(repo_root)),
        },
    }

    return mapping.get(need)
