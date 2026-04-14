import MetaTrader5 as mt5
from risk_engine import calculate_sl_tp
from journal import log_trade

def place_trade(signal, df):
    symbol = "EURUSD"

    if not mt5.initialize():
        return

    tick = mt5.symbol_info_tick(symbol)
    if tick is None:
        return

    price = tick.ask if signal == "BUY" else tick.bid
    atr = df['atr'].iloc[-1]

    sl, tp = calculate_sl_tp(price, atr, signal)

    order_type = mt5.ORDER_TYPE_BUY if signal == "BUY" else mt5.ORDER_TYPE_SELL

    request = {
        "action": mt5.TRADE_ACTION_DEAL,
        "symbol": symbol,
        "volume": 0.01,
        "type": order_type,
        "price": price,
        "sl": sl,
        "tp": tp,
        "deviation": 10,
        "magic": 999,
        "comment": "AUTO_SYSTEM",
        "type_time": mt5.ORDER_TIME_GTC,
        "type_filling": mt5.ORDER_FILLING_IOC,
    }

    result = mt5.order_send(request)

    profit = 1 if signal == "BUY" else -1
    log_trade(signal, price, profit)

    print("Trade executed:", result)
