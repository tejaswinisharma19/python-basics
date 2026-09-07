transaction_amount = int(input())

if transaction_amount <= 1000:
    transaction_fees = transaction_amount * 1 / 100

elif transaction_amount <= 5000:
    transaction_fees = transaction_amount * 2 / 100

else:
    transaction_fees = transaction_amount * 3 / 100

print(transaction_fees)