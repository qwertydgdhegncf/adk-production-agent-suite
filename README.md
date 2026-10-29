# ADK Production Agent Suite

A multi-agent reference project built with Google Agent Development Kit (ADK). The suite demonstrates lead research, Gemini CLI integration, MCP-based bug assistance, automated code review, and e-commerce workflows.

## Project Goals

This project demonstrates how to:

- Build modular agents with Google ADK
- Connect agents to local tools
- Use Gemini CLI inside an ADK pipeline
- Integrate MCP-style tools for software assistance
- Create structured code-review outputs
- Implement product search, cart, and checkout workflows
- Organize an agent project for testing and future cloud deployment

## Included Agents

| Agent | Description | Local command |
|---|---|---|
| Lead Researcher | Creates a structured company and lead research brief | `python -m apps.lead_researcher` |
| Gemini CLI Pipeline | Invokes Gemini CLI as a controlled tool inside an agent pipeline | `python -m apps.gemini_cli_agent` |
| Bug Assistant | Helps inspect symptoms, reproduce issues, and explain possible fixes | `python -m apps.bug_assistant` |
| Code Review Assistant | Produces severity-ranked findings and improvement suggestions | `python -m apps.code_review` |
| Commerce Agent | Supports product discovery, cart operations, and order workflows | `python -m apps.commerce` |

## Repository Structure

```text
adk-production-agent-suite/
├── apps/
│   ├── bug_assistant/
│   ├── code_review/
│   ├── commerce/
│   ├── gemini_cli_agent/
│   └── lead_researcher/
├── common/
│   ├── config.py
│   └── adk_helpers.py
├── data/
│   └── products.json
├── docs/
│   ├── SETUP.md
│   └── VIDEO_WALKTHROUGH.md
├── tests/
├── .env.example
├── pyproject.toml
├── requirements.txt
└── README.md
