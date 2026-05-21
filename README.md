# Binance Futures Testnet Trading Bot

## Setup
1. Clone the repo
2. `python -m venv venv && source venv/bin/activate`
3. `pip install -r requirements.txt`
4. Copy `.env.example` to `.env` and add your testnet API keys

## Usage
```bash
# Market order
python cli.py order --symbol BTCUSDT --side BUY --type MARKET --quantity 0.01

# Limit order
python cli.py order --symbol BTCUSDT --side SELL --type LIMIT --quantity 0.01 --price 50000
```

## Assumptions
- Uses Binance Futures Testnet only (not real funds)
- Minimum quantity for BTCUSDT is 0.001