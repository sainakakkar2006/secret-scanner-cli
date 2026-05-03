from __future__ import annotations

import json
from pathlib import Path

from .scanner import Finding


def findings_to_json(findings: list[Finding]) -> str:
    payload = {
        "total_findings": len(findings),
        "findings": [finding.to_dict() for finding in findings],
    }
    return json.dumps(payload, indent=2, sort_keys=True)


def findings_to_text(findings: list[Finding]) -> str:
    if not findings:
        return "No secrets found."

    lines = [f"{len(findings)} finding(s)", ""]
    for finding in findings:
        lines.extend(
            [
                f"{finding.path}:{finding.line} [{finding.severity}] {finding.rule}",
                f"  value: {finding.value}",
                "",
            ]
        )
    return "\n".join(lines).rstrip()


def write_report(content: str, out_path: str | Path) -> None:
    path = Path(out_path)
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(content + "\n", encoding="utf-8")

