def screen_stock(stock, df):
    return {
        "volume_rank": "Top 10%" if df['Volume'].iloc[-1] > df['Volume'].mean() else "Average",
        "momentum": "High" if df['Close'].iloc[-1] > df['Close'].mean() else "Low"
    }