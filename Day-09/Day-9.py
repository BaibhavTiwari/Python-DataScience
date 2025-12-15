import pandas as pd 

df = pd.read_csv("day9_data.csv")
df["Date"] = pd.to_datetime(df["Date"])
df = df.set_index("Date")

df["Return"] = df["Close"].pct_change()
df = df.dropna() # drop first NaN returns and any other NaNs
print(df.head())
print(df.isna().sum())

# 2. Feature engineering: MAs and volatility

df["MA_5"] = df["Close"].rolling(5).mean()
df["MA_10"] = df["Close"].rolling(10).mean()
df["Vol_10"] = df["Return"].rolling(10).std()

df = df.dropna()
print(df[["Close", "MA_5", "MA_10", "Vol_10"]].head())

# 3. Simple MA crossover strategy

df["Signal"] = 0
df.loc[df["MA_5"] > df["MA_10"], "Signal"] = 1
df["Position"] = df["Signal"].shift(1).fillna(0)

df["Strat_Return"] = df["Position"] * df["Return"]
print(df[["Return", "Position", "Strat_Return"]].head(15))

'''
Basic Backtest Skeleton : Feature -> Rule -> Strategy Returns.
'''

# 4. Evaluate strategy vs buy & hold

df["Cum_Market"] = (1 + df["Return"]).cumprod()
df["Cum_Strat"] = (1 + df["Strat_Return"]).cumprod()

print(df[["Cum_Market", "Cum_Strat"]].tail())

if df.empty:
    print("❌ DataFrame is empty after feature engineering")
    exit()


#comparing final values

market_final = df["Cum_Market"].iloc[-1]
strat_final = df["Cum_Strat"].iloc[-1]
print("Final Market multiple:", market_final)
print("Final Strategy multiple:", strat_final)

# also computing mean and std.

print("Market mean/std:", df["Return"].mean(), df["Return"].std())
print("Strat mean/std:", df["Strat_Return"].mean(), df["Strat_Return"].std())
