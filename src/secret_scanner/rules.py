from __future__ import annotations

import re
from dataclasses import dataclass


@dataclass(frozen=True)
class Rule:
    name: str
    severity: str
    pattern: re.Pattern[str]
    secret_group: str = "secret"


RULES = [
    Rule(
        name="AWS access key",
        severity="HIGH",
        pattern=re.compile(r"(?P<secret>AKIA[0-9A-Z]{16})"),
    ),
    Rule(
        name="GitHub token",
        severity="HIGH",
        pattern=re.compile(r"(?P<secret>gh[pousr]_[A-Za-z0-9_]{20,})"),
    ),
    Rule(
        name="Slack token",
        severity="HIGH",
        pattern=re.compile(r"(?P<secret>xox[baprs]-[A-Za-z0-9-]{20,})"),
    ),
    Rule(
        name="Private key block",
        severity="HIGH",
        pattern=re.compile(r"(?P<secret>-----BEGIN [A-Z ]*PRIVATE KEY-----)"),
    ),
    Rule(
        name="Environment assignment with secret-like name",
        severity="MEDIUM",
        pattern=re.compile(
            r"(?i)\b(?P<secret>(?:api[_-]?key|secret|password|token)\s*=\s*['\"]?[^'\"\s#]+)"
        ),
    ),
    Rule(
        name="High entropy token",
        severity="LOW",
        pattern=re.compile(r"(?P<secret>\b[A-Za-z0-9+/]{32,}={0,2}\b)"),
    ),
]

