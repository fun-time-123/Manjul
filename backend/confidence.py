def generate_confidence_score(indicators, patterns, sentiment, backtest):
    score = 0
    score += 20 if indicators['RSI'] < 70 and indicators['RSI'] > 30 else -10
    score += 20 if indicators['MACD'] == "Bullish" else -5
    score += 15 if patterns['confidence'] == "High" else 0
    score += 10 if sentiment['news'] == "Positive" else 0
    score += 10 if sentiment['twitter'] == "Slightly Bullish" else 0
    score += 15 if backtest['30_day_win_rate'] == "82%" else 0
    return f"{min(95, score)}%"