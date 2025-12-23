## Confidence intervals on returns (Day 15)

- **Confidence interval for a mean**: A range of values constructed from sample data that is likely to contain the true population mean with a chosen confidence level (e.g., 95%); for returns, it brackets plausible values for the true average return.

- **Standard error (SE) of the mean**: The standard deviation of the sampling distribution of the mean, calculated as sample standard deviation divided by the square root of sample size; it measures how much the sample mean is expected to vary from sample to sample.

- **t-critical value (`t_crit`)**: A cutoff value from the t-distribution that depends on the confidence level and degrees of freedom; multiplied by the standard error to determine the margin of error in a confidence interval.

- **95% confidence interval formula**: For a mean, it is often written as  
  \( \text{CI} = \bar{x} \pm t_{\alpha/2, n-1} \times \text{SE} \),  
  where \( \bar{x} \) is the sample mean, \( t_{\alpha/2, n-1} \) is the t-critical value, and SE is the standard error.

## Hypothesis testing on mean return

- **Null hypothesis (\(H_0\))**: The default assumption that there is no effect or no difference; for returns, often \(H_0\!: \mu = 0\), meaning the true mean return is zero.

- **Alternative hypothesis (\(H_1\))**: The competing claim against the null; for returns, this could be \( \mu \neq 0 \) (two-sided) or \( \mu > 0 \) (one-sided) when testing if there is a positive edge.

- **One-sample t-test**: A statistical test that compares the sample mean to a hypothesized population mean (such as 0) using the t-statistic, to decide if the difference is statistically significant given sample variability.

- **t-statistic**: A standardized measure of how far the sample mean is from the hypothesized mean in units of standard error; larger absolute values indicate stronger evidence against the null hypothesis.

- **p-value**: The probability, under the null hypothesis, of observing a test statistic at least as extreme as the one computed from the sample; a small p-value (e.g., < 0.05) suggests that the observed mean is unlikely to be due to random chance alone.
