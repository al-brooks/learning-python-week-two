# Grocery App

def greeting():
    print("\nWelcome to our Grocery List App.\nPlease review the upcoming options carefully:\n")

def farewell():
    print("\nThanks for using our App!\nGoodbye!")

def view_stores():
    print("\nBelow are your stores:")
    print("------------------------------------------------")
    # for i in range(len(shopping_lists)):
    #     print(f"{i + 1}: {shopping_lists[i].name}")

    # Another way to view stores
    for index in range(0, len(shopping_lists)):
        store = shopping_lists[index] # storing array item in new var
        print(f"{index + 1}: {store.name}")
    print("------------------------------------------------")

def view_grocery_items():
    print("\nBelow are your groceries:")
    print("------------------------------------------------")
    # for i in range(len(shopping_lists)):
    #     print(f"{i + 1}: {shopping_lists[i].name}")
    #     for item in shopping_lists[i].items:
    #         print(f"    -> {item.total}")

    # Using new loop similar to view_stores:
    for index in range(0, len(shopping_lists)):
        store = shopping_lists[index] # storing array item in new var
        print(f"{index + 1}: {store.name}")
        for item in store.items:
            print(f"    -> {item.total}")
    print("------------------------------------------------")

class Stores:
    def __init__(self, store, address = "1200 Lakeview Ave"):
        self.name = name
        self.address = address
        self.items = [] # Items will be appended to array

class Groceries:
    def __init__(self, product, price, quantity):
        self.product = product
        self.price = price
        self.quantity = quantity
        self.total = f"{product}, Quantity: {quantity} Units, Total Price: ${price * quantity}"

greeting()
shopping_lists = []

while True:
    print("""
    Please select one of the following:
    A: Create a new list by entering the store information
    B: Add grocery items to a list
    C: View all your shopping lists
    D: Delete a store list
    E: Delete an item from a list
    Q: Exit the program
""")

    selection = input("Enter your selection: ")
    selection = selection.lower()

    # Creating a list:
    if selection == "a":
        name = input("Enter the name of the store: ")
        address = input("Enter the address of the store: ")
        store = Stores(name, address)
        shopping_lists.append(store)
        view_stores()

    elif selection == "b":
        view_stores()
        store_i = int(input("Which store number do you want to edit? "))
        store = shopping_lists[store_i - 1]
        product = input("Enter product name: ")
        price = int(input("Enter item price: "))
        quantity = int(input("Enter how many: "))
        item = Groceries(product, price, quantity)
        store.items.append(item)
        view_grocery_items()

    elif selection == "c":
        view_stores() 
        view_grocery_items()

    elif selection == "d":
        view_stores() 
        store_i = int(input("Which store number do you want to delete? "))
        del shopping_lists[store_i - 1]
        view_stores()

    elif selection == "e":
        view_grocery_items()
        store_i = int(input("Which store number do you want to edit? "))
        store = shopping_lists[store_i - 1]
        print(f"\nBelow are the groceries listed for: {store.name}")
        print("------------------------------------------------")
        for index in range(len(store.items)):
            print(f"{index + 1}: {store.items[index].total}")
        print("------------------------------------------------")
        grocery_del = int(input("Which grocery number do you want to delete?"))
        del store.items[grocery_del - 1]
        view_grocery_items()

    elif selection == "q":
        break

    else:
        print("Please enter A,B,C or q")


farewell()