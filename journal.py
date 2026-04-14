import csv
from datetime import datetime

def log_trade(signal, price, result):
    with open("trades.csv", "a", newline="") as f:
        writer = csv.writer(f)
        writer.writerow([datetime.now(), signal, price, result])
