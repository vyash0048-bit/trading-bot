import os
import hmac
import hashlib
import time
import requests
from dotenv import load_dotenv
from bot.logging_config import setup_logger

load_dotenv()
logger = setup_logger()

BASE_URL = "https://testnet.binancefuture.com"

class BinanceClient:
    def __init__(self):
        self.api_key = os.getenv("BINANCE_API_KEY")
        self.api_secret = os.getenv("BINANCE_API_SECRET")

        if not self.api_key or not self.api_secret:
            raise EnvironmentError("API key/secret not found in .env file")

        self.session = requests.Session()
        self.session.headers.update({"X-MBX-APIKEY": self.api_key})
        logger.info("BinanceClient initialized successfully")

    def _sign(self, params: dict) -> dict:
        params["timestamp"] = int(time.time() * 1000)
        query = "&".join(f"{k}={v}" for k, v in params.items())
        signature = hmac.new(
            self.api_secret.encode(), query.encode(), hashlib.sha256
        ).hexdigest()
        params["signature"] = signature
        return params

    def post(self, endpoint: str, params: dict) -> dict:
        url = f"{BASE_URL}{endpoint}"
        signed = self._sign(params)
        logger.debug(f"POST {url} | params: {signed}")

        try:
            resp = self.session.post(url, params=signed, timeout=10)
            data = resp.json()
            logger.debug(f"Response: {data}")

            if "code" in data and data["code"] != 200:
                logger.error(f"API error: {data}")
                raise ValueError(f"API Error {data['code']}: {data.get('msg', 'Unknown')}")

            return data

        except requests.exceptions.ConnectionError:
            logger.error("Network error: Cannot connect to Binance testnet")
            raise
        except requests.exceptions.Timeout:
            logger.error("Request timed out")
            raise