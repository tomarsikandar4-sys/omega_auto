import pandas as pd
from ai_model import train

def analyze_performance():
    try:
        df = pd.read_csv("trades.csv")
        return df.iloc[:, -1].sum()
    except:
        return 0

def auto_improve(df):
    performance = analyze_performance()

    if performance < 0:
        print("Improving model...")
        train(df)
