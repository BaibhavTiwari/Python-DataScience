#  a function is a named block of code that takes input(parameters), does some work and can give back an output(return value). it helps avpid repetition and keeps logic clean.

''' def function_name(parameters):
   #body
   return result '''

def square(x):
    return x * x
print(square(5))  # 25


# 1.single-trade P&L

def trade_pnl(buy_price, sell_price,quantity):
  pnl =  (sell_price - buy_price) * quantity
  return pnl

p = trade_pnl(100,106,89)
print("P&L", p)


# 2.add fees

def trade_pnl_with_fee(buy_price,sell_price,quantity,fee_per_trade):
  gross = (sell_price - buy_price) * quantity
  net = gross - fee_per_trade
  return net

x = trade_pnl_with_fee(10,20,100,2)
print("Total with fees per trade:", x)


# 3.function for daily P&L from lists

def daily_pnl(buy_price, sell_price, quantity):
  pnl_list = []
  for i in range(len(buy_price)):
    pnl = (sell_price[i] - buy_price[i]) * quantity[i]
    pnl_list.append(pnl)
  return pnl_list

buy_price = [100,90,80]
sell_price = [ 120,130,140]
quantity = [10,59,60]

pnl_list = daily_pnl(buy_price,sell_price,quantity)
print(pnl_list)


# 4. Function to compute returns list

def compute_returns(prices):
  returns = []
  for i in range(1,len(prices)):
    prev_price = prices[i-1]
    curr_price = prices[i]
    r = (curr_price - prev_price) / prev_price
    returns.append(r)
  return returns

prices = [100, 102, 101, 198, 876]
retrurns = compute_returns(prices)
print(retrurns)


# 5. Small classification function

def classify_pnl(pnl):
    if pnl > 0:
        return "Profit"
    elif pnl < 0:
        return "Loss"
    else:
        return "Break-even"

for x in pnl_list:
  print(x, "-", classify_pnl(x))


# 6. Day-4 mini-project: all-in-one daily report

def daily_report(buy_price, sell_price, quantity):
  pnl_list = daily_pnl(buy_price, sell_price, quantity)
  total = sum(pnl_list)
  avg = total / len(pnl_list)
  best = max(pnl_list)
  worst = min(pnl_list)
  return {
    "pnl_list" : pnl_list,
    "total" : total,
    "average" : avg,
    "Best" : best,
    "worst" : worst,
  }

report = daily_report(buy_price, sell_price, quantity)
print(report)