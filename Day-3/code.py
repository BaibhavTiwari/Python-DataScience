# Computing returns from price list.abs

prices = [100, 102, 101, 103, 104]
returns  = []

for i in range(1, len(prices)):
  prev_price = prices[i-1]
  curr_price = prices[i]
  r = (curr_price - prev_price)/ prev_price
  returns.append(r)
print(returns)
print(len(prices))

# returns with comprehension
returns = [
  (prices[i] - prices[i-1])/prices[i-1]
  for i in range(1, len(prices))
]
print(returns)

# range(1, len(prices)) : gives indices from 1 up to last index, so that you always have a “previous” element at i-1.
# returns becaomes a list of daily percentage changes between consecutive prices.