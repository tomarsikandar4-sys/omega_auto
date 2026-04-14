def calculate_sl_tp(price, atr, signal):
    if signal == "BUY":
        sl = price - atr * 1.5
        tp = price + atr * 3
    else:
        sl = price + atr * 1.5
        tp = price - atr * 3

    return sl, tp
