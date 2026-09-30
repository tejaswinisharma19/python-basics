class BankAccount:
    def __init__(self,account_holder,account_number,balance):
        self.account_holder = account_holder
        self.account_number = account_number
        self._balance = balance
        
        
   
    def deposit(self, amount):
        if amount > 0:
            self._balance += amount
            print("updated balance: ",self._balance)
                
        else:
            print("enter valid amount")
        
    def withdraw(self, amount):
        if amount > 0 and amount <= self._balance:
            self._balance -= amount
            print("Updated balance: ",self._balance)
        else:
            print("Insufficient balance or invalid amount")
                
                
        
    def display_account_details(self):
        print("Account Holder:",self.account_holder)
        print("Account Number:",self.account_number)
        print("Current Balance:",self._balance)
        
        
client1 = BankAccount("Winnie", 123456789, 5000)
client2 = BankAccount("Alice", 987654321, 3000)

clients = [client1, client2]
client1.deposit(1000)
client1.withdraw(2000)
client1.withdraw(10000)

client2.deposit(500)
client2.withdraw(1000)
for client in clients:
    client.display_account_details()
    