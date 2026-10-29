import json
from pathlib import Path
from typing import Any


def search_products(query: str, data_file: str = "data/products.json") -> dict:
    products = json.loads(Path(data_file).read_text())
    terms = query.lower().split()
    matches = [p for p in products if any(t in json.dumps(p).lower() for t in terms)]
    return {"query": query, "products": matches[:20]}


def get_product(product_id: str, data_file: str = "data/products.json") -> dict:
    products = json.loads(Path(data_file).read_text())
    for product in products:
        if product["id"] == product_id:
            return product
    return {"error": "Product not found", "product_id": product_id}


def calculate_cart(items: list[dict[str, Any]], data_file: str = "data/products.json") -> dict:
    """Validate quantities and calculate a transparent cart total."""
    products = {p["id"]: p for p in json.loads(Path(data_file).read_text())}
    lines, total = [], 0.0
    for item in items:
        product = products.get(str(item.get("product_id")))
        quantity = int(item.get("quantity", 0))
        if not product:
            return {"ok": False, "error": f"Product not found: {item.get('product_id')}"}
        if quantity < 1 or quantity > 20:
            return {"ok": False, "error": "Quantity must be between 1 and 20"}
        line_total = round(float(product["price"]) * quantity, 2)
        total += line_total
        lines.append({"product_id": product["id"], "name": product["name"],
                      "quantity": quantity, "unit_price": product["price"],
                      "line_total": line_total})
    return {"ok": True, "items": lines, "subtotal": round(total, 2),
            "currency": "USD", "checkout_required": True}


def create_order_preview(items: list[dict[str, Any]], email: str, data_file: str = "data/products.json") -> dict:
    """Create a non-payment order preview; never charges or places an order."""
    cart = calculate_cart(items, data_file)
    if not cart.get("ok"):
        return cart
    return {"ok": True, "order_status": "PENDING_CHECKOUT", "email": email,
            "cart": cart, "message": "Payment and fulfillment require an external checkout integration."}
