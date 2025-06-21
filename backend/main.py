from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from indicators import analyze_indicators
from ai_pattern import detect_patterns
from sentiment import analyze_sentiment
from screener import screen_stock
from confidence import calculate_confidence
from backtest import run_backtest

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"]
)

@app.get("/")
def home():
    return {"message": "Kuhu Intraday API is running"}

@app.get("/analyze")
def analyze(stock: str):
    indicators = analyze_indicators(stock)
    patterns = detect_patterns(stock)
    sentiment = analyze_sentiment(stock)
    screen = screen_stock(stock)
    confidence = calculate_confidence(indicators, patterns, sentiment)
    backtest = run_backtest(stock)

    return {
        "stock": stock.upper(),
        "indicators": indicators,
        "patterns": patterns,
        "sentiment": sentiment,
        "screener": screen,
        "confidence_score": confidence,
        "backtest": backtest
    }
