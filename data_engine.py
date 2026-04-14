import MetaTrader5 as mt5
import pandas as pd
from indicators import add_indicators

def get_data(symbol="EURUSD"):
    if not mt5.initialize():
        print("MT5 init failed")
        return None

    rates = mt5.copy_rates_from_pos(symbol, mt5.TIMEFRAME_M15, 0, 500)

    if rates is None:
        print("No data")
        return None

    df = pd.DataFrame(rates)
    df = add_indicators(df)

    return df
