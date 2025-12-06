# Lists = ordered collection of items in [...]. think of them as a column of values (prices, P&L, quantities). 

prices = [ 100, 105, 101.2, 103, 63]
print(prices)
print(prices[0])
print(prices[-1])

# Slicing

print(prices[1:4])
print(prices[:3])
print(prices[3:])

# Modifying Lists

prices[0]= 99.5
prices.append(105)
prices.remove(101.2)
print(prices)

# Basic analytics on lists

pnl = [120, -50, 30, 20-20, 70,-10]
total_pnl = sum(pnl)
trade_count = len(pnl)
AvgPL = total_pnl/trade_count
best_trade = max(pnl)
worst_trade = min(pnl)
print(total_pnl, AvgPL,best_trade,worst_trade)

#manual mean

pnl = [120, -50, 30, 20-20, 70,-10]
total = 0;
for x in pnl:
  total += x
avg = total/len(pnl)
print(avg)