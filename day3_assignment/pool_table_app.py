# Pool table management app

# Need to track date/time:
from datetime import datetime

# TIME TRACKING TESTING
# ==============================================================================
start = datetime.now() # once indicator is flagged both times should be now()
end = "2021-07-14 19:31:28"
start_str = start.strftime("%Y-%m-%d %H:%M:%S") # convert now() into string

conv_start = datetime.strptime(start_str, "%Y-%m-%d %H:%M:%S")
conv_end = datetime.strptime(end, "%Y-%m-%d %H:%M:%S")
print(conv_end - conv_start)

# ==============================================================================

# time_lapse_s = time_lapse.total_seconds()

# print(now.strftime("%b %d %Y %I:%M:%S %p"))

# You should be able to see all the tables (12)
# need to create a separate table instance - like store or groceries. Store in an array?

tables = [] # global array


# tables should have table number
# start with not being occupied
# can have table methods for switching between on/off - checkout
# two functions within pool table class - checkout with a flag indicator that adds in start time
# checkin function would have an indicator flag and adds in checkout time

# each table in list should 