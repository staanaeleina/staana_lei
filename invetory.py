class Supplier:
    def __init__(self, name, nickname, age, contact_number, email, address):
        self.name = name
        self.nickname = nickname
        self.age = age
        self.contact_number = contact_number
        self.email = email
        self.address = address

    

class Biscuit:
    def __init__(self, name, description, barcode, category, expiration_date, manufacturing_date, price, quantity) -> None:
        self.name = name
        self.description = description
        self.barcode = barcode
        self.category = category
        self.expiration_date = expiration_date
        self.manufacturing_date = manufacturing_date
        self.price = price
        self.quantity = quantity

class Chip:
    def __init__(self, name, description, barcode, category, expiration_date, manufacturing_date, price, quantity):
        self.name = name
        self.description = description
        self.barcode = barcode
        self.category = category
        self.expiration_date = expiration_date
        self.manufacturing_date = manufacturing_date
        self.price = price
        self.quantity = quantity

class Drink:
    def __init__(self, name, description,  barcode, category, expiration_date, manufacturing_date, price, quantity):
        self.name = name
        self.description = description
        self.barcode = barcode
        self.category = category
        self.expiration_date = expiration_date
        self.manufacturing_date = manufacturing_date
        self.price = price
        self.quantity = quantity

class CannedGood:
    def __init__(self, name, description,  barcode, category, expiration_date, manufacturing_date, price, quantity):
        self.name = name
        self.description = description
        self.barcode = barcode
        self.category = category
        self.expiration_date = expiration_date
        self.manufacturing_date = manufacturing_date
        self.price = price
        self.quantity = quantity

class Bread:
    def __init__(self, name, description, barcode, category, expiration_date, manufacturing_date, price, quantity):
        self.name = name
        self.description = description
        self.barcode = barcode
        self.category = category
        self.expiration_date = expiration_date
        self.manufacturing_date = manufacturing_date
        self.price = price
        self.quantity = quantity

class Store:
    def __init__(self):
        self.products = []

    def add_product(self, product):
        self.products.append(product)

    def display_products(self):
        for product in self.products:
            print(f"Product Name: {product.name}")
            print(f"Description: {product.description}")
            print(f"Barcode: {product.barcode}")
            print(f"Category: {product.category}")
            print(f"Expiration Date: {product.expiration_date}")
            print(f"Manufacturing Date: {product.manufacturing_date}")
            print(f"Price: {product.price:.2f}")
            print(f"Quantity: {product.quantity}")
            print("""
""")

    def replace_expired_products(self, current_date):
        new_products = []
        for product in self.products:
            if product.expiration_date >= current_date:
                new_products.append(product)
            else:
                print(f" {product.name} has expired and will be replaced.")
                # Replace the expired product with a new one here
                # You can create a new product instance with a new expiration date and add it to the new_products list

store = Store()
supplier1 = Supplier("Laura Cruz", "Lau", "25", "0909 948 4808", "lauc@gmailcom", "Poblacion, Pandi, Bulacan")
supplier2 = Supplier("Lheon Blythe", "Lheo", "27", "0915 408 6907", "lheoleheon@gmail.com", "San Roque, Pandi, Bulacan")

biscuit = Biscuit("Skyflakes", "Light, flaky and buttery...", "1 56784 78657 9", "biscuit", "2023-01-02", "2021-01-02", 199.00, 5)
chip = Chip("Ridges", "The chips have a ridged or wavy...", "8 97867 56476 2", "chip", "2023-09-08", "2021-10-15", 34.00, 5)
drink = Drink("Gatorade", "a brand of noncarbonated sports drink designed to supply the body with carbohydrates and replace fluids and sodium lost during exertion.", "8 67564 34567 0", "drink", "2023-12-16", "2021-12-16", 32.00, 8)
canned_good = CannedGood("Spam", "made of a pork and ham mixture, salt, sugar, potato starch, water, and sodium nitrite", " 2 34523 76564 8", "canned goods", "2023-08-04", "2020-08-04", 159.00, 6)
bread = Bread("Gardenia", "good taste, freshness, softness, oven-baked aroma and nutritive value", "1 23456 56789 0", "bread", "2023-11-15", "2021-11-15", 135.00, 4)

store.add_product(biscuit)
store.add_product(chip)
store.add_product(drink)
store.add_product(canned_good)
store.add_product(bread)

# Assuming the current date is "2023-09-15"
current_date = "2023-09-15"

store.display_products()
# Replace expired products

print(""" EXPIRED PRODUCTS
--------------------------------------------""")
store.replace_expired_products(current_date)


