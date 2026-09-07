units = int(input())

if units <= 100:
    bill = units * 5

elif units <= 200:
    bill = 500 + (units - 100) * 7

else:
    bill = 1200 + (units - 200) * 10

print(bill)