prices = [7, 1, 5, 3, 6, 4]

buy = prices[0]
profit = 0

for price in prices:
    if price < buy:
        buy = price

    if price - buy > profit:
        profit = price - buy

print(profit)