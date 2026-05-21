from bot.logging_config import setup_logger

logger = setup_logger()

VALID_SIDES = ["BUY", "SELL"]
VALID_ORDER_TYPES = ["MARKET", "LIMIT"]

def validate_inputs(symbol: str, side: str, order_type: str,
                    quantity: float, price: float = None):
    errors = []

    if not symbol or len(symbol) < 3:
        errors.append("Symbol must be a valid pair like BTCUSDT")

    if side.upper() not in VALID_SIDES:
        errors.append(f"Side must be one of: {VALID_SIDES}")

    if order_type.upper() not in VALID_ORDER_TYPES:
        errors.append(f"Order type must be one of: {VALID_ORDER_TYPES}")

    if quantity <= 0:
        errors.append("Quantity must be a positive number")

    if order_type.upper() == "LIMIT":
        if price is None or price <= 0:
            errors.append("Price is required and must be positive for LIMIT orders")

    if errors:
        for e in errors:
            logger.error(f"Validation error: {e}")
        raise ValueError("\n".join(errors))

    logger.info(f"Validation passed: {symbol} {side} {order_type} qty={quantity} price={price}")