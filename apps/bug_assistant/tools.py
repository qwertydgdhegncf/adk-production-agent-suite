from pathlib import Path


def list_workspace_files(workspace: str = "workspace/bug-assistant") -> dict:
    root = Path(workspace).resolve()
    if not root.exists():
        return {"workspace": str(root), "files": []}
    return {"workspace": str(root), "files": [str(p.relative_to(root)) for p in root.rglob("*") if p.is_file()]}


def read_workspace_file(path: str, workspace: str = "workspace/bug-assistant") -> dict:
    root = Path(workspace).resolve()
    candidate = (root / path).resolve()
    if root not in candidate.parents and candidate != root:
        return {"ok": False, "error": "Path escapes the workspace"}
    if not candidate.is_file():
        return {"ok": False, "error": "File not found"}
    return {"ok": True, "path": str(candidate.relative_to(root)), "content": candidate.read_text(errors="replace")}
