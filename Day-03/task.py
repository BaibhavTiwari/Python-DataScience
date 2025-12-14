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

#For each pnl in your P&L list, print “Big profit”, “Small profit”, “Small loss”, “Big loss” based on thresholds you choose (e.g. >50, between 0 and 50, etc.).

pnl = [120, -50, 30, 10, -20, 70, -10]

big_loss_count = 0

for x in pnl:
    if x > 50:
        print(x, "→ Big profit")
    elif x > 0:
        print(x, "→ Small profit")
    elif x >= -50:
        print(x, "→ Small loss")
    else:
        print(x, "→ Big loss")
        big_loss_count += 1

print("Total Big Loss trades:", big_loss_count)

