import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from unittest.mock import patch
from app import create_app
def test_account_balance():
    app = create_app()
    client = app.test_client()

    with patch("app.bot.BasicBot.get_balance") as mock_balance:
        mock_balance.return_value = [{"asset": "USDC", "balance": "1000.4001"}]
        res = client.get("/account-balance")
        assert res.status_code == 200
        assert res.json == [{"asset": "USDC", "balance": "1000.4001"}]
    print("passed account balance test ✅")

@patch("app.bot.BasicBot.create_order")
def test_place_order(mock_create_order):
    app = create_app()
    client = app.test_client()
    payload = {
        "symbol": "BTCUSDC",
        "side": "BUY",
        "type": "MARKET",
        "quantity" : 0.001
    }
    mock_create_order.return_value = {"status": "FILLED"}
    res = client.post("/place-order", json=payload)
    assert res.status_code == 200
    assert res.json['message'] == "Order placed Successfully"
    print("passed place order test ✅")

@patch("app.bot.BasicBot.get_position_info")
def test_get_position_info(mock_position_info):
    app = create_app()
    client = app.test_client()
    mock_position_info.return_value = [{"symbol": "BTCUSDC", "positionAmt": "0.001"}]
    res = client.get("/position")
    assert res.status_code == 200
    assert res.json == [{"symbol": "BTCUSDC", "positionAmt": "0.001"}]
    print("passed position info test ✅")

@patch("app.bot.BasicBot.cancel_order")
def test_cancel_order(mock_cancel_order):
    app = create_app()
    client = app.test_client()
    mock_cancel_order.return_value = {"status": "CANCELLED"}
    res = client.delete("/cancel-order?order_id=123456&symbol=BTCUSDC")
    assert res.status_code == 200
    assert "Future order cancelled" in res.json['message']
    print("passed cancel order test ✅")

def test_home():
    app = create_app()
    client = app.test_client()
    res = client.get("/")
    assert res.status_code == 200
    assert res.json['message'] == "The Trading bot is running."
    print("passed home test ✅")
if __name__ == "__main__":
    test_home()
    test_account_balance()
    test_place_order()
    test_get_position_info()
    test_cancel_order()
