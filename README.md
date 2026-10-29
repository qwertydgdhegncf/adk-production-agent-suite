# ADK Production Agent Suite

Production-oriented reference implementations built with Google ADK, MCP, Gemini CLI, and cloud-native deployment patterns.

## Agents

| Agent | Purpose | Local entrypoint |
|---|---|---|
| Lead Researcher | Researches a company and produces a qualified lead brief | `python -m apps.lead_researcher` |
| Gemini CLI Pipeline | Uses Gemini CLI as a controlled ADK tool | `python -m apps.gemini_cli_agent` |
| Bug Assistant | Uses MCP tools to inspect and explain software bugs | `python -m apps.bug_assistant` |
| Code Review Assistant | Performs structured, severity-ranked code review | `python -m apps.code_review` |
| Commerce Agent | Product discovery, cart, and order workflow | `python -m apps.commerce` |

## Quick start

```bash
cp .env.example .env
python -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
pytest -q
```

Set `GOOGLE_API_KEY` or configure Vertex AI in `.env` before running the agents. Never commit `.env`, API keys, access tokens, customer data, or generated reports.

Detailed setup, architecture, deployment, and the video walkthrough script are in [`docs/`](docs/).
