class BankAccount:

    def __init__(self, account_holder, balance):
        self.account_holder = account_holder
        self._balance = balance

    @property
    def balance(self):
        return self._balance

    @balance.setter
    def balance(self, new_balance):

        if new_balance >= 0:
            self._balance = new_balance
            print("Balance updated successfully.")
        else:
            print("Balance cannot be negative.")


# Create account
account = BankAccount("Winnie", 5000)

# Read balance using property
print("Account Holder:", account.account_holder)
print("Current Balance:", account.balance)

# Update with valid balance
account.balance = 15000
print("Updated Balance:", account.balance)

# Try invalid balance
account.balance = -5000
print("Final Balance:", account.balance)