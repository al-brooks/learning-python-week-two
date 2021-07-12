# Grocery App
# Global Functions
def view_stores():
    print("\nBelow are your current stores.\n")
    for i in range(len(shopping_lists)):
        print(f"Store {i + 1} is {shopping_lists[i].name}")

def view_grocery_items():
    print("\nBelow are you current items:\n")
    for i in range(0, len(shopping_lists)):
        print(shopping_lists[i].name)
        for item in shopping_lists[i].items:
            print(item.total)

# Classes for List and Items:
class Stores:
    def __init__(self, store, address):
        self.name = name
        self.address = address
        self.items = [] # Items will be appended to array

class Groceries:
    def __init__(self, product, price, quantity):
        self.product = product
        self.price = price
        self.quantity = quantity
        self.total = f"{product}: Quantity: {quantity}, Total Price ${price * quantity}"

shopping_lists = []

print("Welcome to our Grocery List App.\nPlease review the upcoming options carefully:\n")

while True:
    print("""
    Please select one of the following:
    A: Create a new list by entering the store information
    B: Add grocery items to a list
    C: View all your shopping lists
    Q: Exit the program
""")

    selection = input("Enter your selection: ")

    # Creating a list:
    if selection.lower() == "a":
        name = input("Enter the name of the store: ")
        address = input("Enter the address of the store: ")
        store = Stores(name, address)
        shopping_lists.append(store)
        view_stores()

    elif selection.lower() == "b":
        view_stores()
        store_i = int(input("Which store number do you want to edit? "))
        product = input("Enter product name: ")
        price = int(input("Enter item price: "))
        quantity = int(input("Enter how many: "))
        item = Groceries(product, price, quantity)
        shopping_lists[store_i - 1].items.append(item)

    elif selection.lower() == "c":
        view_stores() 
        

    elif selection.lower() == "q":
        break

    else:
        print("Please enter A,B,C or q")


print("Goodbye")