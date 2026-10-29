"""Deterministic research tools that can be replaced by a search provider."""

from __future__ import annotations

import re
from urllib.parse import quote_plus

import httpx


def company_research_query(company: str, industry: str = "") -> dict:
    """Return search queries and an evidence checklist for a company."""
    subject = f"{company} {industry}".strip()
    return {
        "company": company,
        "queries": [
            f"{subject} official website",
            f"{subject} products customers funding",
            f"{subject} leadership news partnerships",
        ],
        "evidence_fields": ["company", "industry", "products", "customers", "signals", "sources"],
    }


def fetch_public_page(url: str, max_chars: int = 6000) -> dict:
    """Fetch a public web page with bounded size and no credentials."""
    if not re.match(r"^https?://", url, re.I):
        return {"ok": False, "error": "Only http(s) URLs are allowed"}
    try:
        response = httpx.get(url, timeout=15, follow_redirects=True)
        response.raise_for_status()
    except httpx.HTTPError as exc:
        return {"ok": False, "error": str(exc)}
    text = re.sub(r"\s+", " ", response.text)
    return {"ok": True, "url": str(response.url), "status_code": response.status_code,
            "content": text[:max_chars]}


def build_lead_brief(company: str, research_notes: str, target_buyer: str = "") -> dict:
    """Create a structured lead brief from evidence supplied by the agent."""
    return {
        "company": company,
        "target_buyer": target_buyer or "Not specified",
        "qualification": "Needs human validation",
        "evidence": research_notes,
        "recommended_next_step": "Validate the decision maker and send a personalized outreach message.",
        "confidence": "medium" if research_notes.strip() else "low",
    }
