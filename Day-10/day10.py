from backtest import load_price_data, ma_crossover_signals

df = load_price_data("day10.csv")
df = ma_crossover_signals(df, short=5, long=10)
