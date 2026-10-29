from common.adk_helpers import llm_agent
from .tools import list_workspace_files, read_workspace_file


root_agent = llm_agent(
    name="mcp_bug_assistant",
    instruction="""
You are a bug-assistance agent. Use the workspace tools to inspect only files relevant to a reported
bug. Reproduce the issue conceptually, identify likely root causes, distinguish evidence from guesses,
and propose a minimal safe fix plus tests. Do not reveal secrets found in files. Return a triage summary,
evidence, root-cause hypotheses ranked by confidence, reproduction steps, and remediation.
""",
    tools=[list_workspace_files, read_workspace_file],
)
