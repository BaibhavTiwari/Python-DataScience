## Day 9 – Key Definitions

### Data Cleaning
- **Missing values (NaN)**: Special markers used in Pandas to represent missing or undefined data; they must usually be handled (dropped or filled) before analysis or modeling. [web:73][web:107]
- **dropna()**: Pandas function that removes rows (or columns) containing NaN values, often used to clean a dataset before computing features or running strategies. [web:73][web:107]

### Feature Engineering
- **Feature**: A measurable input variable used by a model or rule, such as price, return, moving average, or volatility; features encode information from raw data. [web:107][web:110]
- **Rolling window**: A sliding subset of consecutive rows (e.g., last 5 or 10 days) used to compute statistics like mean or standard deviation over time. [web:97][web:100]
- **Moving Average (MA)**: The average of a price over a fixed rolling window (e.g., 5 days); it smooths short‑term fluctuations and highlights trends. [web:97][web:100]
- **Short MA (e.g., MA_5)**: A moving average computed over a smaller window (like 5 days), which reacts faster to recent price changes. [web:97]
- **Long MA (e.g., MA_10)**: A moving average computed over a larger window (like 10 days), which changes more slowly and represents the longer‑term trend. [web:97]
- **Rolling volatility (rolling std)**: The rolling standard deviation of returns over a given window (e.g., 10 days), often used as a measure of recent risk or variability. [web:97][web:109]

### Strategy Logic
- **Signal**: A numeric code (often 1, 0, or -1) representing the trading decision at a time step, such as long, flat, or short. [web:101][web:105]
- **Position**: The actual exposure taken (e.g., 1 for long, 0 for flat), often defined as the previous day’s signal so trades are executed on the next bar. [web:101][web:105]
- **MA crossover strategy**: A trading rule that enters or exits positions based on the relationship between a short and long moving average, such as going long when the short MA is above the long MA and flat otherwise. [web:75][web:100]
- **Return**: The fractional change in price over a period, often computed as \((P_t - P_{t-1}) / P_{t-1}\), representing percentage gain or loss. [web:76][web:106]
- **Strategy return (Strat_Return)**: The return obtained when applying a position to market returns, typically `Position * Return` for long‑only strategies. [web:75][web:97]

### Performance Metrics
- **Cumulative return (cumprod of 1+return)**: The growth factor of an investment over time computed as the cumulative product of \((1 + \text{return})\), showing how 1 unit of capital evolves. [web:76][web:109]
- **Buy & hold (market) return**: The cumulative return from buying the asset at the start and holding it without trading, used as a baseline benchmark. [web:75][web:110]
- **Strategy equity curve**: The time series of cumulative strategy returns (e.g., `Cum_Strat`), representing the value of the strategy portfolio over time. [web:107][web:110]
- **Volatility (std of returns)**: The standard deviation of returns over a period, used as a statistical measure of the variability or risk of an asset or strategy. [web:97][web:109]
