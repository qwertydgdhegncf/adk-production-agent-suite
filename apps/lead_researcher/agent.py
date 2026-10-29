from common.adk_helpers import llm_agent

from .tools import build_lead_brief, company_research_query, fetch_public_page


root_agent = llm_agent(
    name="deep_lead_researcher",
    instruction="""
You are a deep research lead-generation agent. Research companies using public evidence only.
Separate verified facts from hypotheses, cite URLs supplied by tools, identify likely business pain,
buying signals, target personas, and a concise outreach angle. Never invent funding, customers,
employees, or contact information. Return: executive summary, evidence table, qualification score,
risks, recommended next step, and source URLs.
""",
    tools=[company_research_query, fetch_public_page, build_lead_brief],
)
