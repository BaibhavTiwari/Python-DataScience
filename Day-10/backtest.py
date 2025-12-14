import pandas as pd
import numpy as np

def load_price_data(path: str) -> pd.DataFrame:
    df = pd.read_csv(path)
    df["Date"] = pd.to_datetime(df["Date"])
    df = df.set_index("Date")

    df["Return"] = df["Close"].pct_change()
    df = df.dropna().copy()   # 👈 explicit copy

    return df


def add_ma_features(df: pd.DataFrame, short: int = 5, long: int = 10) -> pd.DataFrame:
    df = df.copy()  # 👈 defensive copy

    df.loc[:, f"MA_{short}"] = df["Close"].rolling(short).mean()
    df.loc[:, f"MA_{long}"] = df["Close"].rolling(long).mean()

    return df.dropna().copy()


def ma_crossover_signals(df: pd.DataFrame, short: int = 5, long: int = 10) -> pd.DataFrame:
    df = add_ma_features(df, short, long).copy()

    signal_col = "Signal"

    df.loc[:, signal_col] = 0
    df.loc[df[f"MA_{short}"] > df[f"MA_{long}"], signal_col] = 1

    df.loc[:, "Position"] = df[signal_col].shift(1).fillna(0)
    df.loc[:, "Strat_Return"] = df["Position"] * df["Return"]

    return df
