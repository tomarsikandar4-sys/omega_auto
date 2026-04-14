from data_engine import get_data
from ai_model import train, predict
from strategy import generate_signal

df = get_data()

if df is not None:
    if train(df):
        pred, conf = predict(df)
        signal, _ = generate_signal(df)

        print("Prediction:", pred)
        print("Confidence:", conf)
        print("Signal:", signal)
    else:
        print("Training error")
else:
    print("Data error")
