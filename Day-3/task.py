# Print each P&L with a label: "Trade P&L:", like Trade P&L: 120
pnl = [120, -50, 30, 10, -20, 70, -10]
for x in pnl:
    print("Trade P&L:",x)

# Count how many trades are profitable using a loop and a counter variable.
pnl = [120, -50, 30, 10, -20, 70, -10]

profit_count = 0

pnl = [120, -50, 30, 10, -20, 70, -10]

profit_count = 0
loss_count = 0

for x in pnl:
    if x > 0:
        profit_count += 1
        print("Profit trade #", profit_count, "P&L:", x)
    elif x < 0:
        loss_count += 1
        print("Loss trade   #", loss_count, "P&L:", x)
    else:
        print("Break-even trade. P&L:", x)

print("Total profit trades:", profit_count)
print("Total loss trades:  ", loss_count)
