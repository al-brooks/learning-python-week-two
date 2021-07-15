from datetime import datetime
from classes import PoolTable
import json  

pool_tables = []
checked_out = []

def create_tables():
    for table in range(1, 13):
        pool_table = PoolTable(table)
        pool_tables.append(pool_table)

def display_status():
    print("\n\tBelow are all pool tables:")
    print("\t=========================================\n")
    for table in pool_tables:
        print(f"\tTable # {table.number}")
        print(f"\tTable is {table.occupy_status()}")
        print(f"\tCheck-out Time is {table.start_time_display}\n")

def display_occupied():
    print("\n\tBelow are the occupied tables:")
    print("\t=========================================\n")
    for table in pool_tables:
        if table.is_occupied == True:
            print(f"\tTable # {table.number}")
            print(f"\tTable is {table.occupy_status()}")
            print(f"\tCheck-out Time is {table.start_time_display}\n")
        else:
            continue

def display_not_occupied():
    print("\n\tBelow are the open tables:")
    print("\t=========================================\n")
    for table in pool_tables:
        if table.is_occupied == False:
            print(f"\tTable # {table.number}")
            print(f"\tTable is {table.occupy_status()}")
            print(f"\tCheck-out Time is {table.start_time_display}\n")
        else:
            continue

# Initiate pool_table objects
create_tables()

while True:
    print("\n\tPlease choose one of the options below:")
    print("\t==========================================\n")
    print("\tA. Check out pool table")
    print("\tB. Check in pool table")
    print("\tC. View pool tables")
    print("\tQ. Quit App\n")

    choice = input("\tEnter your choice:    ")
    choice = choice.upper()

    # Check out pool table
    if choice == "A":
        display_not_occupied()
        table_num = int(input("\tEnter the table # you want to check out:   "))

        # pull table num from array
        user_table = pool_tables[table_num -1]

        # run check_out method
        user_table.check_out()
        print(f"\tYour start time is: {user_table.start_time_display}\n")
    
    if choice == "B":
        # display all tables
        display_occupied()

        # which table do they want to check out
        table_num = int(input("\tEnter the table # you want to check in:    "))

        # pull table num from array
        user_table = pool_tables[table_num -1]

        # run check_out method
        user_table.check_in()
        checked_out.append(user_table.check_in_to_dict())
        user_table.attribute_reset()
        # print(f"Your start time is: {user_table.start_time_display}")

    if choice == "C":
        # display all tables
        display_status()


    if choice == "Q":
        break

# Check dict array
# print(checked_out)
with open("pool_tables_activity.json", "w") as file:
            json.dump(checked_out, file)
# table_1.check_out()
# print(table_1.start_time)

# ==============================================================================




# tables should have table number
# start with not being occupied
# can have table methods for switching between on/off - checkout
# two functions within pool table class - checkout with a flag indicator that adds in start time
# checkin function would have an indicator flag and adds in checkout time

# each table in list should 