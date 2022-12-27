from sys import stdin
import sys
from typing import List, Tuple

# --------------------------- VENDING MACHINE ----------------------------------------------

class ProductOutOfStock(Exception):
    pass


class ProductDontExist(Exception):
    pass


class Product:

    def __init__(self, name: str, price: int) -> None:
        self.name = name 
        self.price = price


class VMStock:

    def __init__(self) -> None:
        self.products = []

    def add_or_update_product_in_stock(self, product: Product, quantity: int) -> None:
        """
        Check if a product exists, if exists updated the quantity in stock.
        If it doesnt exist create a new record
        - Quantity can be positive or negative
        """
        if len(self.products) > 0 :
            for index, p in enumerate(self.products):
                if p['product'].name == product.name:
                    self.products[index]['quantity'] += quantity

                    return

        # Add product to array if it doesn't exist
        self.products.append({'product': product, 'quantity': quantity})


class VMEmpty(Exception):
    pass


class VendingMachine:

    def __init__(self, stock: VMStock):
        self.stock = stock 

    def select_product(self, product: Product) -> Tuple[int, int]:
        """
        Customer selects a product        
        This f returns index, price
        """
        for index, p in enumerate(self.stock.products):
            if p.get_name() == product.name and p.stock >= 1:
                return index, p.price
            else:
                raise ProductOutOfStock 

        
        raise VMEmpty


    def buy_product(self, index: int) -> None:
        """
        Customer buys a single product of the machine
        """
        try:
            self.stock.products[index].quantity -= 1
        except:
            raise ProductDontExist 

# --------------------------- CUSTOMER ---------------------------------------------------

class Customer:

    def __init__(self, name: str, inserted_money: str):
        self.name = name
        self.inserted_money = inserted_money


# --------------------------- INITIALIZATION ---------------------------------------------
INITIAL_STOCK = VMStock()

INITIAL_STOCK.add_or_update_product_in_stock(
    product=Product(
        name = "coca-cola",
        price = 12,
    ),
    quantity=3
)

INITIAL_STOCK.add_or_update_product_in_stock(
    product=Product(
        name = "fanta",
        price = 10,
    ),
    quantity=5
)

INITIAL_STOCK.add_or_update_product_in_stock(
    product=Product(
        name = "kitkat",
        price = 15,
    ),
    quantity=7
)


INITIAL_STOCK.add_or_update_product_in_stock(
    product=Product(
        name = "terrabusi",
        price = 5,
    ),
    quantity=2
)


INITIAL_STOCK.add_or_update_product_in_stock(
    product=Product(
        name = "lays",
        price = 15,
    ),
    quantity=2
)



def main():

    while True:
        print("\n Welcome to our vending machine \n")
        print("You are a customer or a admin? \n")
        print("- Press 1 for customer")
        print("- Press 2 for admin")
        print("- Press 3 for exit \n")
        try:
            type_of_person = int(input())
        except:
            print("Please insert a number \n")
            continue


        if type_of_person == 3:
            sys.exit(1)

        if type_of_person == 1:
            while True:
                print("\n What would you like to do \n")
                print("- Press 1 for list of products")
                print("- Press 2 to buy a product")
                print("- Press 3 to exit")

                try:
                    option = int(input())
                except:
                    print("Please insert a number \n")
                    continue

                if option == 3:
                    break

                if option == 1:
                    for p in INITIAL_STOCK.products:
                        print(f"- Name: {p['product'].name} -- Price: {p['product'].price}")
                        continue
                if option == 2:
                    print("Please insert the name of the product \n")
                    product = input()

                    product_index = -100
                    for index, p in enumerate(INITIAL_STOCK.products):
                        if p['product'].name == product:
                            product_index = index

                    if product_index == -100:
                        print("That product doesn't exist in the machine")
                        continue


                    print("Please insert the money for the product \n")
                    try:
                        money = int(input())
                    except:
                        print("Please insert a number \n")
                        continue

                    product_price = INITIAL_STOCK.products[product_index]['product'].price

                    if money < product_price:
                        print("The money you entered is less than the price of the product \n")
                        continue

                    INITIAL_STOCK.products.pop(product_index)
                    rest = money - product_price

                    print(f"This is your rest {rest}")

        if type_of_person == 2:
            while True:
                print("\n What would you like to do \n")
                print("- Press 1 add or update a product")
                print("- Press 2 to exit")

                try:
                    option = int(input())
                except:
                    print("Please insert a number \n")
                    continue

                if option == 2:
                    break

                if option == 1:
                    print("Please insert the name of the product \n")
                    product = input()

                    product_index = -100
                    for index, p in enumerate(INITIAL_STOCK.products):
                        if p['product'].name == product:
                            product_index = index

                    if product_index == -100:
                        print("Please insert the price \n")
                        try:
                            price = int(input())
                        except:
                            print("Please insert a number \n")
                            continue

                        print("Please insert the quantity \n")
                        try:
                            quantity = int(input())
                        except:
                            print("Please insert a number \n")
                            continue

                        product = Product(name=product, price=price)

                        INITIAL_STOCK.add_or_update_product_in_stock(product, quantity)
                    else:
                        try:
                            print("Please insert the quantity \n")
                            quantity = int(input())
                        except:
                            print("Please insert a number \n")
                            continue

                        INITIAL_STOCK.add_or_update_product_in_stock(INITIAL_STOCK.products[product_index]['product'], quantity)



main()
