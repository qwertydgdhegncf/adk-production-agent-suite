from google.adk.agents import LlmAgent

from common.config import settings


def llm_agent(*, name: str, instruction: str, tools=None) -> LlmAgent:
    """Create agents consistently so model configuration is centralized."""
    return LlmAgent(
        name=name,
        model=settings().model,
        instruction=instruction,
        tools=tools or [],
    )
