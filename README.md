cat > README.md << 'EOF'
# Binance Futures Testnet Trading Bot

A Python CLI bot to place Market and Limit orders on Binance Futures Testnet (USDT-M).

## Setup

1. Clone the repo:
```bash
   git clone https://github.com/vyash0048-bit/trading-bot.git
   cd trading-bot
```
2. Create and activate virtual environment:
```bash
   python -m venv venv
   source venv/bin/activate   # Windows: venv\Scripts\activate
```
3. Install dependencies:
```bash
   pip install -r requirements.txt
```
4. Configure API keys:
```bash
   cp .env.example .env
   # Edit .env and add your Binance Futures Testnet API key and secret
```

## How to Run

### Market Order
```bash
python cli.py --symbol BTCUSDT --side BUY --type MARKET --quantity 0.01
```

### Limit Order
```bash
python cli.py --symbol BTCUSDT --side SELL --type LIMIT --quantity 0.01 --price 75000
```

### All Options
