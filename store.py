class Product:
    def __init__(self, brandname, price, quantity):
        self.brandname = brandname
        self.price = price
        self.quantity = quantity

    def display(self):
        print(f"{self.brandname} - ${self.price:.2f}  [Quantity:{self.quantity}]")
    
    def decrease_quantity(self, number):
        if self.quantity >= number:
            self.quantity -= number

class Customer:
    def __init__(self, name):
        self.name = name
        self.cart =[]

    def add_to_cart(self, product):
        self.cart.append(product)

    def check_cart(self):
        print(f"""
{self.name}'s Shopping Cart:""")
        print("--------------------------------")
        for product in self.cart:
            product.display()

class Cashier:
    def __init__(self, customer):
        self.customer = customer

    def total_price(self):
        total =sum(product.price for product in self.customer.cart)
        return total
    
    def checkout(self, payment_amount):
        total = self.total_price()
        if payment_amount >= total:
            change = payment_amount - total
            print("-------------------------------------------------------")
            print(f"Payment successful! Your change is ${change:.2f} ")
            print("""Thanks for buying!
            

            """)
        else:
            print("--------------------------------------------------------")
            print(f"Payment unsuccessful. You don't have enough money")
            print(f"""Total cost: ${total:.2f}
            
            """)

class Store:
    def __init__(self, name):
        self.name = name
        self.products = []

    def add_product(self, product):
        self.products.append(product)

    def list_products(self):
        for product in self.products:
            product.display()

if __name__ == "__main__":
    store = Store("Biscuit Store")

    product1 = Product("Skyflakes", 95.00, 10)
    product2 = Product("Wafer Time", 155.00, 20)
    product3 = Product("Rebisco", 80.00, 15)
    product4 = Product("Oreo", 281.00, 9)


    customer1 = Customer("Remi")
    customer1.add_to_cart(product1)

    product1.decrease_quantity(1)

    customer1.check_cart()

    store.list_products()

    cashier = Cashier(customer1)

    payment_amount = 100.00
    cashier.checkout(payment_amount)

    
    customer2 = Customer("Ziggy")
    customer2.add_to_cart(product1)
    customer2.add_to_cart(product4)

    product1.decrease_quantity(1)
    product4.decrease_quantity(1)

    customer2.check_cart()

    store.list_products()

    cashier = Cashier(customer2)

    payment_amount = 300.00
    cashier.checkout(payment_amount)

    customer3 = Customer("Finn")
    customer3.add_to_cart(product2)
    customer3.add_to_cart(product1)
    customer3.add_to_cart(product3)

    product2.decrease_quantity(1)
    product1.decrease_quantity(1)
    product3.decrease_quantity(1)

    customer3.check_cart()

    store.list_products()

    cashier = Cashier(customer3)

    payment_amount = 500.00
    cashier.checkout(payment_amount)










