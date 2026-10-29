import json
from pathlib import Path


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
