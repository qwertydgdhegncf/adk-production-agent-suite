import os
import sys

from common.adk_helpers import llm_agent
from .tools import list_workspace_files, read_workspace_file

from google.adk.tools.mcp_tool import McpToolset
from google.adk.tools.mcp_tool.mcp_session_manager import StdioConnectionParams
from mcp import StdioServerParameters


mcp_toolset = McpToolset(
    connection_params=StdioConnectionParams(
        server_params=StdioServerParameters(
            command=sys.executable,
            args=["-m", "mcp_server"],
            env={**os.environ, "PYTHONPATH": os.getcwd()},
        ),
        timeout=30,
    ),
    tool_name_prefix="bug_mcp_",
)


root_agent = llm_agent(
    name="mcp_bug_assistant",
    instruction="""
You are a bug-assistance agent. Use the workspace tools to inspect only files relevant to a reported
bug. Reproduce the issue conceptually, identify likely root causes, distinguish evidence from guesses,
and propose a minimal safe fix plus tests. Do not reveal secrets found in files. Return a triage summary,
evidence, root-cause hypotheses ranked by confidence, reproduction steps, and remediation.
""",
    tools=[list_workspace_files, read_workspace_file, mcp_toolset],
)
