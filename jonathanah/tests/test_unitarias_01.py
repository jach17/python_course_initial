from unittest.mock import Mock
import pytest
from src.unitarias_01 import get_user_data, apply_discount

def test_get_user_data_ok(monkeypatch):
    mock_response = Mock(status_code=200)
    mock_response.json.return_value = {"id": 1, "name": "Arqui"}

    monkeypatch.setattr("requests.get", lambda url: mock_response)

    result = get_user_data(1)
    assert result["name"] == "Arqui"
    
def test_apply_discount_normal():
    """Debe aplicar correctamente el descuento."""
    total = apply_discount(100.0, 10.0)
    assert total == 90.0  # 100 - 10%