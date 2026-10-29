# ADK Production Agent Suite

Production-oriented reference implementations built with Google ADK, MCP, Gemini CLI, and cloud-native deployment patterns.

This repository is a runnable reference suite: each agent exposes an ADK `root_agent`, local tools are
tested deterministically, and external side effects such as payments, CRM writes, and file mutation are
explicitly gated.

## Agents

| Agent | Purpose | Local entrypoint |
|---|---|---|
| Lead Researcher | Researches public company evidence and produces a qualified lead brief | `adk web apps/lead_researcher` |
| Gemini CLI Pipeline | Uses Gemini CLI as a controlled ADK tool | `adk web apps/gemini_cli_agent` |
| Bug Assistant | Uses safe workspace tools and the standalone MCP server to inspect and explain software bugs | `adk web apps/bug_assistant` |
| Code Review Assistant | Performs structured, severity-ranked code review | `adk web apps/code_review` |
| Commerce Agent | Product discovery, cart totals, and a non-payment order preview | `adk web apps/commerce` |

## Quick start

```bash
cp .env.example .env
python -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
python -m pytest -q
```

Set `GOOGLE_API_KEY` or configure Vertex AI in `.env` before running the agents. Never commit `.env`, API keys, access tokens, customer data, or generated reports.

Detailed setup, architecture, deployment, and the video walkthrough script are in [`docs/`](docs/).

## Demonstrated safety boundaries

- Lead research labels evidence versus inference and uses public URLs only.
- Gemini CLI has an explicit working directory and timeout.
- Bug tools reject workspace path traversal.
- Code review includes deterministic secret and shell-risk checks before an LLM review.
- Commerce returns a transparent cart and `PENDING_CHECKOUT` preview; it never processes payment.
- The MCP server runs over stdio and exposes narrowly scoped tools.
