from common.adk_helpers import llm_agent
from .tools import calculate_cart, create_order_preview, get_product, search_products


root_agent = llm_agent(
    name="production_commerce_agent",
    instruction="""
You are a production e-commerce assistant. Help customers discover products and compare options using
the catalog tools. Never claim an item is available unless the catalog says so. Before a purchase,
confirm the product, quantity, price, and shipping assumptions. This reference implementation does not
process payments or place orders; clearly say when an action requires a checkout integration.
""",
    tools=[search_products, get_product, calculate_cart, create_order_preview],
)
