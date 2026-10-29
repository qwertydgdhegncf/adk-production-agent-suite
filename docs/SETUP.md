# Setup and execution

## 1. Install

```bash
python3.11 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
cp .env.example .env
```

Set `GOOGLE_API_KEY` for the Gemini Developer API, or set `GOOGLE_GENAI_USE_VERTEXAI=true` together
with Google Cloud authentication for Vertex AI.

## 2. Run tests and lint

```bash
pytest -q
ruff check .
```

## 3. Run an agent

The ADK web UI can discover an agent package from the repository root. For example:

```bash
adk web apps/lead_researcher
adk web apps/code_review
```

The lead researcher is also an ADK package:

```bash
adk web apps/lead_researcher
```

Run the standalone MCP server over stdio:

```bash
python -m mcp_server
```

It exposes `list_files`, `read_file`, and `triage_symptom`, while rejecting path traversal.

The Python modules also expose `root_agent` for embedding in an ADK runner or deployment service.

## Safety notes

The Gemini CLI wrapper is intentionally bounded by a timeout and explicit working directory. The bug
assistant tools reject paths outside the configured workspace. Payment, order placement, email sending,
and CRM writes are deliberately not implemented in this starter foundation.
