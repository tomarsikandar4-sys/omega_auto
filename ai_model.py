import numpy as np
from sklearn.ensemble import RandomForestClassifier

model = RandomForestClassifier(n_estimators=100, random_state=42)
trained = False

def prepare_data(df):
    df = df.copy()

    df['target'] = np.where(df['close'].shift(-5) > df['close'], 1, 0)
    df = df.dropna()

    features = ['close','ema20','ema50','rsi','atr','tick_volume']

    X = df[features]
    y = df['target']

    return X, y

def train(df):
    global trained

    X, y = prepare_data(df)

    if len(X) < 50:
        return False

    split = int(len(X) * 0.8)

    model.fit(X[:split], y[:split])
    trained = True

    return True

def predict(df):
    if not trained:
        return None, 0

    last = df.iloc[-1:]
    X = last[['close','ema20','ema50','rsi','atr','tick_volume']]

    pred = model.predict(X)[0]
    conf = model.predict_proba(X)[0].max()

    return pred, conf
