"""Small deterministic checks used before an LLM review."""

from __future__ import annotations

import re


def review_text(source: str, filename: str = "snippet") -> dict:
    """Find high-signal security and reliability patterns without executing code."""
    findings = []
    patterns = [
        (r"(?:api[_-]?key|secret|password)\s*=\s*['\"]", "BLOCKER", "Possible hard-coded secret"),
        (r"subprocess\.(?:run|Popen|call)\([^\n]*shell\s*=\s*True", "HIGH", "Shell injection risk"),
        (r"except\s*:\s*(?:pass|\.\.\.)", "MEDIUM", "Exception is swallowed"),
        (r"print\([^\n]*(?:token|password|secret)", "HIGH", "Sensitive value may be logged"),
    ]
    for pattern, severity, title in patterns:
        for match in re.finditer(pattern, source, flags=re.I):
            line = source.count("\n", 0, match.start()) + 1
            findings.append({"severity": severity, "title": title, "file": filename,
                             "line": line, "evidence": source.splitlines()[line - 1].strip(),
                             "recommendation": "Remove the secret or use a validated safe abstraction."})
    return {"filename": filename, "findings": findings,
            "summary": f"{len(findings)} deterministic finding(s); follow with an LLM review."}
