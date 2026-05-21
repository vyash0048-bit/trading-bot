# Binance Futures Testnet Trading Bot

A Python CLI bot to place Market and Limit orders on Binance Futures Testnet (USDT-M).

## Setup

1. Clone the repo:
   git clone https://github.com/vyash0048-bit/trading-bot.git
   cd trading-bot

2. Create virtual environment:
   python -m venv venv
   venv\Scripts\activate

3. Install dependencies:
   pip install -r requirements.txt

4. Configure API keys:
   Copy .env.example to .env and add your Binance Futures Testnet credentials

## How to Run

Market Order:
   python cli.py --symbol BTCUSDT --side BUY --type MARKET --quantity 0.01

Limit Order:
   python cli.py --symbol BTCUSDT --side SELL --type LIMIT --quantity 0.01 --price 75000

Options:
   --symbol    Trading pair e.g. BTCUSDT
   --side      BUY or SELL
   --type      MARKET or LIMIT
   --quantity  Order quantity
   --price     Required for LIMIT orders only

## Project Structure

trading_bot/
  bot/
    client.py          Binance API client wrapper
    orders.py          Order placement logic
    validators.py      Input validation
    logging_config.py  Logging setup
  cli.py               CLI entry point
  logs/                API request and response logs
  .env.example         Environment variable template
  requirements.txt

## Assumptions
- Uses Binance Futures Testnet only (not real funds)
- Minimum quantity for BTCUSDT is 0.001
- SELL LIMIT price must be above current market price
- BUY LIMIT price must be below current market price
- Logs written to logs/trading_bot.log
