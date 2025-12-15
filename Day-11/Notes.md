## Simulation Concepts

- **Simulated returns**: Artificially generated return values produced using a statistical model or distribution (for example, drawing daily returns from a normal distribution) to study how a price series might behave under certain assumptions without relying only on historical data.
- **Normal distribution (for returns)**: A continuous probability distribution defined by a mean and standard deviation, often used as a simple model for daily asset returns where most values cluster near the mean and extreme values are rarer.
- **Daily mean return (`mu_daily`)**: The expected average return per day in a simulation model, used as the central value of the distribution from which daily returns are drawn.
- **Daily volatility (`sigma_daily`)**: The standard deviation of daily returns in a simulation model, controlling how widely returns vary around the mean; higher values produce more volatile price paths.

---

## Simulated Price Paths

- **Simulated price path**: A sequence of hypothetical prices created by compounding simulated returns starting from an initial price, typically using  
  `Price_t = Price_{t-1} × (1 + r_t)` over many time steps.
- **Cumulative product of (1 + returns)**: A method for building a price or wealth path from returns by repeatedly multiplying `(1 + r_t)` across time, which models reinvestment of gains and losses.
- **Random seed (`np.random.seed`)**: A fixed initializer for the random number generator that ensures simulations are reproducible, so running the code again with the same seed produces identical random sequences.

---

## Resampling and Frequency Changes

- **Resampling (time series)**: The process of converting a time series from one frequency to another (such as daily to weekly or monthly) by grouping data into new time buckets and applying an aggregation function like `last`, `mean`, or `sum`.
- **Weekly resampling (`"W"`)**: A resampling rule that groups daily observations into calendar weeks, often using the last available value in each week to represent the weekly close price.
- **Monthly resampling (`"M"`)**: A resampling rule that groups daily observations into calendar months, typically using the last value of each month as the month-end close.
- **Aggregated returns by frequency**: Returns computed after resampling prices (e.g., weekly or monthly percentage changes), which usually show larger standard deviations than daily returns because they cover longer time intervals.
