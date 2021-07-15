# Pool table management app

# Need to track date/time:
from datetime import datetime
from classes import PoolTable        

# Create Table instances
# ==============================================================================
tables = [] # global array

# creates 12 tables instances

for table in range(1, 13):
    pool_table = PoolTable(table)
    tables.append(pool_table)
    # print(pool_table.number) # testing number attribute - works


# view all tables and occupation status
for table in range(1, len(tables) + 1):
    print(pool_table.display_occupy(table))

# You should be able to see all the tables (12)
# need to create a separate table instance - like store or groceries. Store in an array?

# ==============================================================================



# Print out menu options
# ==============================================================================
while True:
    print("""
    A. Check out pool table
    B. Check in pool table
    C. View pool tables
    Q. Quit App
    """)

    choice = input("Enter your choice: ")
    choice = choice.upper()

    # Check out pool table
    if choice == "A":
        # display all tables
        for table in tables:
            print(f"Table # {table.number}")
            print(f"Checkout Time is {table.start_time}")

        # which table do they want to check out
        table_num = int(input("Enter the table # you want to check out"))

        # pull table num from array
        user_table = tables[table_num -1]

        # run check_out method
        user_table.check_out()
        print(f"Your start time is: {user_table.start_time_display}")


    if choice == "Q":
        break


# table_1.check_out()
# print(table_1.start_time)

# ==============================================================================




# tables should have table number
# start with not being occupied
# can have table methods for switching between on/off - checkout
# two functions within pool table class - checkout with a flag indicator that adds in start time
# checkin function would have an indicator flag and adds in checkout time

# each table in list should 