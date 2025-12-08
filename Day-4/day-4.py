#  a function is a named block of code that takes input(parameters), does some work and can give back an output(return value). it helps avpid repetition and keeps logic clean.

''' def function_name(parameters):
   #body
   return result '''

def square(x):
    return x * x
print(square(5))  # 25


#single-trade P&L

def trade_pnl(buy_price, sell_price,quantity):
  pnl =  (sell_price - buy_price) * quantity
  return pnl

p = trade_pnl(100,106,89)
print("P&L", p)


#add fees

def trade_pnl_with_fee(buy_price,sell_price,quantity,fee_per_trade):
  gross = (sell_price - buy_price) * quantity
  net = gross - fee_per_trade
  return net

x = trade_pnl_with_fee(10,20,100,2)
print("Total with fees per trade:", x)


# function for daily P&L from lists

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