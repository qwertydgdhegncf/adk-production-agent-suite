import json

from apps.bug_assistant.tools import read_workspace_file
from apps.commerce.tools import get_product, search_products


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
