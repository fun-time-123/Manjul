from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
import yfinance as yf
from backend.indicators import calculate_indicators
from backend.ai_pattern import detect_patterns
from backend.sentiment import fetch_sentiment
from backend.screener import screen_stock
from backend.backtest import run_backtest
from backend.confidence import generate_confidence_score

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/analyze")
async def analyze(stock: str):
    # 💡 Always get fresh data
    data = yf.download(stock, period="1d", interval="1m", progress=False)
    
    if data.empty:
        return {"error": "No data found. Check symbol or market closed."}

    indicators = calculate_indicators(data)
    pattern = detect_patterns(data)
    sentiment = fetch_sentiment(stock)
    screener = screen_stock(stock, data)
    backtest = run_backtest(stock)
    confidence = generate_confidence_score(indicators, pattern, sentiment, backtest)

    return {
        "stock": stock.upper(),
        "indicators": indicators,
        "patterns": pattern,
        "sentiment": sentiment,
        "screener": screener,
        "confidence_score": confidence,
        "backtest": backtest
    }
