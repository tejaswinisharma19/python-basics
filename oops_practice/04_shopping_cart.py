class Product:
    def __init__(self,name,price,quantity):
        self.name = name
        self.price = price
        self.quantity = quantity
        
    def display_product(self):
        print("Product Name:",self.name)
        print("Price:",self.price)
        print("Quantity:",self.quantity)
        
class ShoppingCart:
    def __init__(self):
        self.cart_items = []

    def add_product(self, Product):
        self.cart_items.append(Product)
        print("Product added to cart:", Product.name)

    def remove_product(self,Product_name):
        for product in self.cart_items:
            if Product_name == product.name:
               self.cart_items.remove(product)
               print("Product removed from cart:", Product_name)
               return 
            
        print("Product not found in cart:", Product_name)
            
    def calculate_total(self):
        total = 0
        
        for product in self.cart_items:
            total += product.price * product.quantity
        return total
    
    def display_cart(self):
        print("\n --- Shopping Cart ---")
        
        for product in self.cart_items:
            product.display_product()
            print()
        cart_total = self.calculate_total()
        print("Total Cart Value:", cart_total)


Product1 = Product("Laptop",5000,1)
Product2 = Product("Mouse",1000,2)
Product3 = Product("Keyboard",2000,1)

cart = ShoppingCart()

cart.add_product(Product1)
cart.add_product(Product2)
cart.add_product(Product3)

cart.display_cart()

cart.remove_product("Mouse")

cart.display_cart()

cart.remove_product("Phone")