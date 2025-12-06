## Python basic data types

- **int (integer)**: Whole numbers without decimal part, used for counts like number of trades (`5`, `-10`, `120`).[2]
- **float (floating point)**: Numbers with decimal part, used for prices, percentages (`3.5`, `102.5`, `-20.75`).[2]
- **bool (boolean)**: Logical values `True` or `False`, often used in conditions or filters (e.g., `pnl > 0`).[2]
- **str (string)**: Text data inside quotes, used for names, symbols, IDs (`"AAPL"`, `"Tanya"`).[2]

***

## Lists and operations

- **List**: An ordered, changeable collection of items written in square brackets, e.g., `prices = [100, 102.5, 101.2]`; used to store sequences like prices or P&L.[3][1]
- **Indexing**: Accessing an element by its position in the list, e.g., `prices[0]` is first element, `prices[-1]` is last.[3]
- **Slicing**: Taking a sub-part of a list using `start:stop`, e.g., `prices[1:4]` gives elements at positions 1,2,3; `prices[:3]` first three; `prices[3:]` from index 3 onward.[1]
- **append()**: List method that adds a new element at the end, e.g., `prices.append(105)` adds `105` to the list.[3]
- **remove()**: List method that deletes the first occurrence of a given value, e.g., `prices.remove(101.2)` removes that value from the list.[3]

***

## Built-in functions on lists

- **len()**: Returns the number of items in a list (`len(pnl)` gives trade count).[4]
- **sum()**: Adds up all numeric elements in a list (`sum(pnl)` gives total P&L).[4]
- **min()**: Returns the smallest element in a list (`min(pnl)` gives worst trade P&L).[4]
- **max()**: Returns the largest element in a list (`max(pnl)` gives best trade P&L).[4]

***

## Loops and manual calculations

- **for loop**: A control structure to repeat a block of code for each item in a sequence, e.g., `for x in pnl:` processes every trade’s P&L one by one.[1]
- **Manual mean (average)**: Process of summing elements and dividing by count:  
  - Initialize `total = 0`  
  - For each `x` in list, do `total += x`  
  - Compute `avg = total / len(list)`; this is the arithmetic mean.[5]

***

## P&L-related definitions

- **P&L (Profit and Loss)**: Profit or loss from a trade or set of trades; for one trade, often computed as \((\text{sell\_price} - \text{buy\_price}) \times \text{quantity}\).[2]
- **Total P&L**: Sum of P&L of all trades in a period, e.g., `sum(pnl_list)` for a day.[4]
- **Average P&L**: Total P&L divided by number of trades, giving the mean profit or loss per trade.[4]
- **Best trade**: Trade with the maximum P&L value (`max(pnl_list)`), the most profitable trade.[4]
- **Worst trade**: Trade with the minimum P&L value (`min(pnl_list)`), the largest loss.[4]
