def detect_patterns(df):
    close = df['Close']
    if close.iloc[-1] > close.iloc[-3] and close.iloc[-2] < close.iloc[-4]:
        return {"pattern": "Breakout", "confidence": "High"}
    return {"pattern": "No Clear Pattern", "confidence": "Low"}