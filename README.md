<div align="center">

<!-- Animated header -->
<img src="https://readme-typing-svg.demolab.com?font=Fira+Code&weight=700&size=32&duration=3000&pause=1000&color=F0B90B&center=true&vCenter=true&width=600&lines=Binance+Futures+Trading+Bot;USDT-M+Testnet+%7C+Python+CLI;Market+%26+Limit+Orders+%E2%9A%A1" alt="Typing SVG" />

<br/>

<!-- Badges -->
![Python](https://img.shields.io/badge/Python-3.x-3776AB?style=for-the-badge&logo=python&logoColor=white)
![Binance](https://img.shields.io/badge/Binance-Futures_Testnet-F0B90B?style=for-the-badge&logo=binance&logoColor=black)
![CLI](https://img.shields.io/badge/CLI-Typer-009688?style=for-the-badge&logo=gnometerminal&logoColor=white)
![License](https://img.shields.io/badge/License-MIT-green?style=for-the-badge)
![Status](https://img.shields.io/badge/Status-Active-brightgreen?style=for-the-badge)

<br/>

<!-- Animated separator -->
<img src="https://user-images.githubusercontent.com/73097560/115834477-dbab4500-a447-11eb-908a-139a6edaec5c.gif" width="100%"/>

</div>

<br/>

## 📌 Overview

A clean, production-ready **Python CLI trading bot** for placing **Market** and **Limit** orders on the **Binance Futures Testnet (USDT-M)**. Built with structured layers, full logging, and robust error handling.

```
┌─────────────────────────────────────────────────┐
│           BINANCE FUTURES TRADING BOT            │
│  ─────────────────────────────────────────────  │
│   ⚡  Market Orders   →   Instant execution      │
│   📋  Limit Orders    →   Price-based triggers   │
│   🔒  Validated Input →   Safe & predictable     │
│   📝  Full Logging    →   Every request logged   │
└─────────────────────────────────────────────────┘
```

<div align="center">
<img src="https://user-images.githubusercontent.com/73097560/115834477-dbab4500-a447-11eb-908a-139a6edaec5c.gif" width="100%"/>
</div>

<br/>

## 🗂️ Project Structure

```
trading_bot/
│
├── 📁 bot/
│   ├── 🔌 client.py          ← Binance API client wrapper
│   ├── 📦 orders.py          ← Order placement logic
│   ├── ✅ validators.py      ← Input validation
│   └── 📝 logging_config.py  ← Logging setup
│
├── 💻 cli.py                 ← CLI entry point (Typer)
├── 📋 logs/                  ← API request & response logs
│   └── trading_bot.log
├── 🔐 .env.example           ← Environment variable template
├── 📦 requirements.txt
└── 📖 README.md
```

<br/>

<div align="center">
<img src="https://user-images.githubusercontent.com/73097560/115834477-dbab4500-a447-11eb-908a-139a6edaec5c.gif" width="100%"/>
</div>

## ⚙️ Setup

### 1️⃣ Clone the Repository

```bash
git clone https://github.com/vyash0048-bit/trading-bot.git
cd trading-bot
```

### 2️⃣ Create Virtual Environment

```bash
# Create
python -m venv venv

# Activate (Windows)
venv\Scripts\activate

# Activate (Mac/Linux)
source venv/bin/activate
```

### 3️⃣ Install Dependencies

```bash
pip install -r requirements.txt
```

### 4️⃣ Configure API Keys

```bash
# Copy the template
cp .env.example .env
```

Then open `.env` and fill in your [Binance Futures Testnet](https://testnet.binancefuture.com) credentials:

```env
BINANCE_API_KEY=your_api_key_here
BINANCE_API_SECRET=your_secret_key_here
```

> 💡 **Get testnet keys:** Register at [testnet.binancefuture.com](https://testnet.binancefuture.com) → Sign in with GitHub → Generate API Key

<br/>

<div align="center">
<img src="https://user-images.githubusercontent.com/73097560/115834477-dbab4500-a447-11eb-908a-139a6edaec5c.gif" width="100%"/>
</div>

## 🚀 How to Run

### ⚡ Market Order

Executes immediately at the current market price.

```bash
python cli.py --symbol BTCUSDT --side BUY --type MARKET --quantity 0.01
```

**Expected output:**
```
──────────────── Order Request Summary ────────────────
  Symbol    : BTCUSDT
  Side      : BUY
  Type      : MARKET
  Quantity  : 0.01
───────────────────────────────────────────────────────
──────────────── ✅ Order Placed Successfully ──────────
┌─────────────┬──────────────┐
│ orderId     │ 4921837641   │
│ status      │ FILLED       │
│ origQty     │ 0.01         │
│ executedQty │ 0.01         │
│ avgPrice    │ 73850.20     │
└─────────────┴──────────────┘
```

### 📋 Limit Order

Waits until the market reaches your target price.

```bash
python cli.py --symbol BTCUSDT --side SELL --type LIMIT --quantity 0.01 --price 75000
```

**Expected output:**
```
──────────────── Order Request Summary ────────────────
  Symbol    : BTCUSDT
  Side      : SELL
  Type      : LIMIT
  Quantity  : 0.01
  Price     : 75000.0
───────────────────────────────────────────────────────
──────────────── ✅ Order Placed Successfully ──────────
┌─────────────┬──────────────┐
│ orderId     │ 4921837642   │
│ status      │ NEW          │  ← Waiting to be filled
│ origQty     │ 0.01         │
│ price       │ 75000.0      │
└─────────────┴──────────────┘
```

<br/>

## 🎛️ All CLI Options

| Option | Required | Description | Example |
|--------|----------|-------------|---------|
| `--symbol` | ✅ | Trading pair | `BTCUSDT` |
| `--side` | ✅ | Direction | `BUY` or `SELL` |
| `--type` | ✅ | Order type | `MARKET` or `LIMIT` |
| `--quantity` | ✅ | Amount to trade | `0.01` |
| `--price` | ⚠️ LIMIT only | Target price | `75000` |

<br/>

<div align="center">
<img src="https://user-images.githubusercontent.com/73097560/115834477-dbab4500-a447-11eb-908a-139a6edaec5c.gif" width="100%"/>
</div>

## 🛡️ Error Handling

The bot gracefully handles all common failure scenarios:

| Error Type | Example | Behaviour |
|---|---|---|
| Missing required field | No `--price` on LIMIT | Clear validation message |
| Invalid side | `--side HOLD` | Rejected before API call |
| Price out of range | SELL below market | API error shown cleanly |
| Network failure | No internet | Caught and logged |
| Invalid API keys | Wrong credentials | Auth error displayed |

<br/>

## 📝 Logging

All activity is automatically logged to `logs/trading_bot.log`:

```
2026-05-21 12:09:30 | INFO     | BinanceClient initialized successfully
2026-05-21 12:09:30 | INFO     | Validation passed: BTCUSDT BUY MARKET qty=0.01
2026-05-21 12:09:30 | INFO     | Placing order: {'symbol': 'BTCUSDT', 'side': 'BUY', ...}
2026-05-21 12:09:31 | DEBUG    | Response: {'orderId': 4921837641, 'status': 'FILLED', ...}
2026-05-21 12:09:31 | INFO     | Order placed successfully. orderId=4921837641, status=FILLED
```

<br/>

<div align="center">
<img src="https://user-images.githubusercontent.com/73097560/115834477-dbab4500-a447-11eb-908a-139a6edaec5c.gif" width="100%"/>
</div>

## 📌 Assumptions

- Uses **Binance Futures Testnet only** — no real funds involved
- Minimum quantity for `BTCUSDT` is `0.001`
- `SELL LIMIT` price must be **above** current market price
- `BUY LIMIT` price must be **below** current market price
- API keys must be from [testnet.binancefuture.com](https://testnet.binancefuture.com) (not live Binance)
- Logs are written to `logs/trading_bot.log`

<br/>

<div align="center">
<img src="https://user-images.githubusercontent.com/73097560/115834477-dbab4500-a447-11eb-908a-139a6edaec5c.gif" width="100%"/>

<br/>

**Built for Primetrade.ai Python Developer Internship Assignment**

![Made with Python](https://img.shields.io/badge/Made%20with-Python-1f425f?style=for-the-badge&logo=python)
![Binance Testnet](https://img.shields.io/badge/Binance-Testnet-F0B90B?style=for-the-badge&logo=binance&logoColor=black)

</div>