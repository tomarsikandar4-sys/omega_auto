import time
from data_engine import get_data
from ai_model import train
from strategy import generate_signal
from execution import place_trade
from auto_improve import auto_improve

def run():
    df = get_data()

    if df is None:
        print("Data error")
        return

    if not train(df):
        print("Training failed")
        return

    print("SYSTEM STARTED")

    while True:
        df = get_data()

        signal, conf = generate_signal(df)

        print("Signal:", signal, "Confidence:", conf)

        if signal is not None:
            place_trade(signal, df)

        auto_improve(df)

        time.sleep(60)

if __name__ == "__main__":
    run()
