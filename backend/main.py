from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
import yfinance as yf
from indicators import calculate_indicators
from ai_pattern import detect_patterns
from sentiment import fetch_sentiment
from screener import screen_stock
from backtest import run_backtest
from confidence import generate_confidence_score

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/analyze")
def analyze(stock: str):
    data = yf.download(stock, period="1d", interval="5m", progress=False)
    if data.empty:
        return {"error": "Stock not found or market closed"}

    indicators = calculate_indicators(data)
    patterns = detect_patterns(data)
    sentiment = fetch_sentiment(stock)
    screener = screen_stock(stock, data)
    backtest = run_backtest(stock)
    confidence = generate_confidence_score(indicators, patterns, sentiment, backtest)

    return {
        "stock": stock.upper(),
        "indicators": indicators,
        "patterns": patterns,
        "sentiment": sentiment,
        "screener": screener,
        "confidence_score": confidence,
        "backtest": backtest
    }