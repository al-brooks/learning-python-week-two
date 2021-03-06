# Grocery App
from classes import Store, Grocery

def greeting():
    print("\nWelcome to our Grocery List App.\nPlease review the upcoming options carefully:\n")

def farewell():
    print("\nThanks for using our App!\nGoodbye!")

def view_stores():
    print("\nBelow are your stores:")
    print("------------------------------------------------")
    for index in range(0, len(shopping_lists)):
        store = shopping_lists[index]
        print(f"{index + 1}: {store.name}")
    print("------------------------------------------------")

def view_grocery_items():
    print("\nBelow are your groceries:")
    print("------------------------------------------------")
    for index in range(0, len(shopping_lists)):
        store = shopping_lists[index]
        print(f"{index + 1}: {store.name}")
        for item in store.items:
            print(f"    -> {item.total}")
    print("------------------------------------------------")

greeting()
shopping_lists = []


while True:
    try:
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
            store = Store(name, address)
            shopping_lists.append(store)
            view_stores()

        elif selection == "b":
            view_stores()
            store_i = int(input("Which store number do you want to edit? "))
            store = shopping_lists[store_i - 1]
            product = input("Enter product name: ")
            price = int(input("Enter item price: "))
            quantity = int(input("Enter how many: "))
            item = Grocery(product, price, quantity)
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

    except ValueError:
        print("Please enter the values prompted on the screen!")

farewell()