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



# Testing loop to see if class methods worked 
# ==============================================================================
# while True:
#     print("Does someone want to check out a pool table?\n")

#     choice = input("Enter in y or n: ")

#     if choice.lower() == "y":
#         table_1 = PoolTable(1)
#         table_1.check_out()
#         print(f"Your start time is: {table_1.start_time_display}")

#     game_over = input("Are they done playing? Enter y or n")

#     if game_over.lower() == "y":
#         table_1.check_in()
#         print(table_1.play_duraton)
#         break


# table_1.check_out()
# print(table_1.start_time)

# ==============================================================================




# tables should have table number
# start with not being occupied
# can have table methods for switching between on/off - checkout
# two functions within pool table class - checkout with a flag indicator that adds in start time
# checkin function would have an indicator flag and adds in checkout time

# each table in list should 