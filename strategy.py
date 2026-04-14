from ai_model import predict

def generate_signal(df):
    if df is None or len(df) < 50:
        return None, 0

    pred, conf = predict(df)

    last = df.iloc[-1]

    trend_up = last['ema20'] > last['ema50']
    rsi_ok = 30 < last['rsi'] < 70

    if pred == 1 and trend_up and rsi_ok and conf > 0.7:
        return "BUY", conf

    if pred == 0 and not trend_up and rsi_ok and conf > 0.7:
        return "SELL", conf

    return None, 0
