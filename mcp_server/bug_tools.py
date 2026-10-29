"""A standalone MCP server exposing safe bug triage tools."""

from pathlib import Path

from mcp.server.fastmcp import FastMCP


mcp = FastMCP("bug-assistance-tools")


@mcp.tool()
def list_files(workspace: str = "workspace/bug-assistant") -> list[str]:
    """List files below a configured bug workspace."""
    root = Path(workspace).resolve()
    return [str(path.relative_to(root)) for path in root.rglob("*") if path.is_file()] if root.exists() else []


@mcp.tool()
def read_file(path: str, workspace: str = "workspace/bug-assistant") -> dict:
    """Read one file while preventing path traversal."""
    root = Path(workspace).resolve()
    candidate = (root / path).resolve()
    if root not in candidate.parents or not candidate.is_file():
        return {"ok": False, "error": "File is outside the workspace or does not exist"}
    return {"ok": True, "path": str(candidate.relative_to(root)), "content": candidate.read_text(errors="replace")}


@mcp.tool()
def triage_symptom(symptom: str) -> dict:
    """Return a structured starting point for a bug report."""
    return {"symptom": symptom, "next_steps": ["capture a minimal reproduction", "collect logs", "write a regression test"]}


if __name__ == "__main__":
    mcp.run(transport="stdio")
