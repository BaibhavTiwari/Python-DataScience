# Definition: a for loop goes through each element of a sequence

pnl = [120, -50, 30, 10, -20, 70, -10]
for x in pnl:
  print(x)

# Conditions let you react differently depending on data.

# if conditions

x=5;
if x>0:
  print("positive")

# if-elif-else

pnl=30
if pnl > 0:
  print("Positive")
elif pnl < 0:
  print("Negative")
else:
  print("Break-even")

# List comprehension = a compact way to build a list from another list with a pattern.
# new_list = [ expression for item in old_list]

pnl = [102, -30, 60]
squared = [x**2 for x in pnl]
print(squared)

returns