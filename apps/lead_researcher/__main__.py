from .agent import root_agent


def main() -> None:
    """Print a usage hint; use `adk web apps/lead_researcher` for the UI."""
    print(f"Loaded ADK agent: {root_agent.name}")
    print("Run: adk web apps/lead_researcher")


if __name__ == "__main__":
    main()
