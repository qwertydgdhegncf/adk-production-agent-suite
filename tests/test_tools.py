import json

from apps.bug_assistant.tools import read_workspace_file
from apps.code_review.tools import review_text
from apps.commerce.tools import calculate_cart, get_product, search_products


def test_product_search(tmp_path):
    data = tmp_path / "products.json"
    data.write_text(json.dumps([{"id": "1", "name": "Blue mug", "category": "home"}]))
    assert search_products("blue", str(data))["products"][0]["id"] == "1"


def test_product_lookup_missing(tmp_path):
    data = tmp_path / "products.json"
    data.write_text("[]")
    assert get_product("missing", str(data))["error"] == "Product not found"


def test_bug_tool_blocks_path_escape(tmp_path):
    assert read_workspace_file("../secret.txt", str(tmp_path))["ok"] is False


def test_cart_total_is_transparent(tmp_path):
    data = tmp_path / "products.json"
    data.write_text(json.dumps([{"id": "1", "name": "Blue mug", "price": 12.5}]))
    result = calculate_cart([{"product_id": "1", "quantity": 2}], str(data))
    assert result["ok"] is True
    assert result["subtotal"] == 25.0


def test_review_flags_hard_coded_secret():
    result = review_text('API_KEY = "do-not-commit"', "app.py")
    assert result["findings"][0]["severity"] == "BLOCKER"
