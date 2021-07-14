# Pool table management app

# Need to track date/time:
from datetime import datetime
from classes import PoolTable

#  Step 1: TIME TRACKING TESTING
# ==============================================================================
start = datetime.now() # once indicator is flagged both times should be now()
end = "2021-07-14 19:31:28"
start_str = start.strftime("%Y-%m-%d %H:%M:%S") # convert start into string

conv_start = datetime.strptime(start_str, "%Y-%m-%d %H:%M:%S") # Str -> datetime
conv_end = datetime.strptime(end, "%Y-%m-%d %H:%M:%S") # Str -> datetime
# print(conv_end - conv_start) # datetime calc in useable format

# now need to take this and convert to mins only when under an hour

# ==============================================================================

# Step 2 - test a class: 
# ==============================================================================
while True:
    print("Does someone want to check out a pool table?\n")

    choice = input("Enter in y or n: ")

    if choice.lower() == "y":
        table_1 = PoolTable(1)
        table_1.check_out()
        print(f"Your start time is: {table_1.start_time_display}")

    game_over = input("Are they done playing? Enter y or n")

    if game_over.lower() == "y":
        table_1.check_in()
        print(table_1.play_duraton)
        break


# table_1.check_out()
# print(table_1.start_time)

# ==============================================================================


# Step 4: 
# ==============================================================================

# You should be able to see all the tables (12)
# need to create a separate table instance - like store or groceries. Store in an array?
tables = [] # global array

# ==============================================================================


# tables should have table number
# start with not being occupied
# can have table methods for switching between on/off - checkout
# two functions within pool table class - checkout with a flag indicator that adds in start time
# checkin function would have an indicator flag and adds in checkout time

# each table in list should 