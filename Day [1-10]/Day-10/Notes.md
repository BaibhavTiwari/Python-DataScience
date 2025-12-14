## Backtest Pipeline Functions

### Data Loader Function (`load_price_data`)
A function that reads raw price data from a CSV file, converts the date column to datetime, sets it as the index, computes returns, drops missing values, and returns a cleaned DataFrame ready for analysis or strategy building.

### Feature Builder Function (`add_ma_features`)
A function that takes a DataFrame and adds new feature columns such as short and long moving averages. This encapsulates feature engineering steps in one reusable and modular place.

### Signal Generator (`ma_crossover_signals`)
A function that applies a trading rule (e.g., short moving average greater than long moving average) to generate trading signals and positions, and then computes strategy returns. This packages the strategy logic into a single callable unit.


## Sharpe Ratio and Risk-Adjusted Return

### Sharpe Ratio
A risk-adjusted performance metric defined as the mean excess return (return above the risk-free rate) divided by the standard deviation of returns. It is often annualized; a higher Sharpe ratio indicates better return per unit of risk.

### Excess Return
The difference between an investment’s return and the risk-free rate over the same period, representing the extra reward earned for taking on risk.

### Annualized Sharpe Ratio
A version of the Sharpe ratio scaled to a yearly basis by multiplying the daily Sharpe ratio by the square root of the number of trading periods per year (commonly 252 for daily data).


## Comparison Metrics

### Strategy Sharpe
The Sharpe ratio computed on the strategy’s return series, used to evaluate how efficiently the strategy converts risk into return compared to other strategies or benchmarks.

### Market (Buy-and-Hold) Sharpe
The Sharpe ratio computed on the asset’s own returns without active trading, used as a baseline risk-adjusted performance metric to assess whether the strategy adds value.
