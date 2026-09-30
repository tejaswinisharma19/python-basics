class Payment:
    def __init__(self,amount):
        self.amount = amount
    
    def pay(self):
        print("Payment of amount:", self.amount)
    
    
    
class UPI(Payment):
    def pay(self):
        print("Payment of amount:",self.amount,"using UPI.")
    
    
    
class CreditCard(Payment):
    def pay(self):
        print("Payment of amount:",self.amount,"using Credit Card.")
    
    
    
class NetBanking(Payment):
    def pay(self):
        print("Payment of amount:",self.amount,"using Net Banking.")
        
        
upi_payment = UPI(10000)
credit_card = CreditCard(200000)
net_banking = NetBanking(500000)

payments = [upi_payment, credit_card, net_banking]

for payment in payments:
    payment.pay()
    