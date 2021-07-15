from datetime import datetime
from classes import PoolTable
import json  

pool_tables = []
tables_checked_in = []

def create_tables():
    for table in range(1, 13):
        pool_table = PoolTable(table)
        pool_tables.append(pool_table)

def main_menu():
    print("\n\tPlease choose one of the options below:")
    print("\t==========================================\n")
    print("\tA. Check out pool table")
    print("\tB. Check in pool table")
    print("\tC. View pool tables")
    print("\tQ. Quit App\n")

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

create_tables()

while True:
    main_menu()

    choice = input("\tEnter Menu Option:    ")
    choice = choice.upper()

    if choice == "A":
        display_not_occupied()
        table_num = int(input("\tEnter the table # you want to check out:   "))
        user_table = pool_tables[table_num -1]
        user_table.check_out()
        print(f"\tYour start time is: {user_table.start_time_display}\n")
    
    if choice == "B":
        display_occupied()
        table_num = int(input("\tEnter the table # you want to check in:    "))
        user_table = pool_tables[table_num -1]
        user_table.check_in()
        tables_checked_in.append(user_table.check_in_to_dict())
        user_table.attribute_reset()
        

    if choice == "C":
        display_status()


    if choice == "Q":
        break

with open("pool_tables_activity.json", "w") as file:
            json.dump(tables_checked_in, file)
