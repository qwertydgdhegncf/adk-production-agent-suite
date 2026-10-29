import asyncio
import os
from pathlib import Path


async def run_gemini_cli(prompt: str, working_directory: str = ".") -> dict:
    """Run Gemini CLI with a timeout and a bounded working directory."""
    binary = os.getenv("GEMINI_CLI_BIN", "gemini")
    timeout = int(os.getenv("GEMINI_CLI_TIMEOUT_SECONDS", "120"))
    workdir = Path(working_directory).resolve()
    if not workdir.is_dir():
        return {"ok": False, "error": f"Working directory does not exist: {workdir}"}
    try:
        process = await asyncio.create_subprocess_exec(
            binary, "-p", prompt,
            cwd=workdir,
            stdout=asyncio.subprocess.PIPE,
            stderr=asyncio.subprocess.PIPE,
        )
        stdout, stderr = await asyncio.wait_for(process.communicate(), timeout=timeout)
    except FileNotFoundError:
        return {"ok": False, "error": f"Gemini CLI not found: {binary}"}
    except asyncio.TimeoutError:
        process.kill()
        await process.wait()
        return {"ok": False, "error": f"Gemini CLI timed out after {timeout}s"}
    return {"ok": process.returncode == 0, "returncode": process.returncode,
            "stdout": stdout.decode(errors="replace"), "stderr": stderr.decode(errors="replace")}
