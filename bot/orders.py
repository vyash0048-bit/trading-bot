from bot.client import BinanceClient
from bot.logging_config import setup_logger

logger = setup_logger()

def place_order(client: BinanceClient, symbol: str, side: str,
                order_type: str, quantity: float, price: float = None) -> dict:

    params = {
        "symbol": symbol.upper(),
        "side": side.upper(),
        "type": order_type.upper(),
        "quantity": quantity,
    }

    if order_type.upper() == "LIMIT":
        params["price"] = price
        params["timeInForce"] = "GTC"  # Good Till Cancelled

    logger.info(f"Placing order: {params}")

    response = client.post("/fapi/v1/order", params)

    logger.info(f"Order placed successfully. orderId={response.get('orderId')}, "
                f"status={response.get('status')}")
    return response