def calculate_indicators(df):
    import pandas_ta as ta
    df['EMA20'] = df['Close'].ewm(span=20, adjust=False).mean()
    df['EMA50'] = df['Close'].ewm(span=50, adjust=False).mean()
    rsi = ta.rsi(df['Close'], length=14).iloc[-1]
    macd = ta.macd(df['Close'])
    macd_signal = "Bullish" if macd['MACD_12_26_9'].iloc[-1] > macd['MACDs_12_26_9'].iloc[-1] else "Bearish"
    vwap = df['Close'].iloc[-1] > df['VWAP_D'].iloc[-1] if 'VWAP_D' in df else "NA"

    return {
        "RSI": round(rsi, 2),
        "MACD": macd_signal,
        "VWAP": "Above" if vwap else "Below",
        "EMA_Crossover": "Bullish" if df['EMA20'].iloc[-1] > df['EMA50'].iloc[-1] else "Bearish"
    }