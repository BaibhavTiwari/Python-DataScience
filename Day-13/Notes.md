## Monte Carlo on strategy returns (Day 13)

- **Strategy return matrix**: A 2D array where each column represents the series of returns from applying a trading strategy to one simulated path, and each row is a time step; used to analyze performance across many scenarios at once.

- **Path-wise performance metrics**: Calculations such as final wealth or Sharpe ratio computed separately for each simulated path, giving a distribution of outcomes rather than a single value.

- **Risk-cut rule (toy example)**: A simple strategy that reduces position size after large negative returns (for example, halving exposure when the previous day’s return is below −2%) to limit downside risk in adverse conditions.

- **Distribution of final wealth**: The spread of ending capital multiples (e.g., 0.8×, 1.1×, 1.5×) across all simulated strategy paths, used to assess how often the strategy performs well or poorly under the modeled assumptions.

- **Distribution of Sharpe ratios**: The set of Sharpe values computed per simulated path, showing how the strategy’s risk‑adjusted performance varies across different simulated market conditions, and helping judge robustness rather than relying on a single backtest.
