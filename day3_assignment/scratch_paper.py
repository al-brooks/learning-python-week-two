from datetime import datetime
import json

# Testing duration display

# time1 = datetime.now()
# time2 = datetime(2021,7,15,0,0,0,0)
# duration = time2 - time1


# duration_secs = duration.total_seconds()
# duration_min = duration_secs / 60
# duration_hour = duration_min / 60

# print("%.0f" % duration_secs)
# print("%.2f" % duration_min)
# print("%.2f" % duration_hour)


# if duration_min < 1:
#     return duration_secs
# elif duration_min >= 1 and duration_min < 60:
#     return duration_min
# elif duration_min > 60:
#     return duration_hour
# else:
#     print("bad code")

# making sure array is appending correctly - looks good

# [
#     {
#         'table_number': 3, 
#         'start_time': '07-15-2021 03:56:30 PM', 
#         'end_time': '07-15-2021 03:56:50 PM', 
#         'play_duration': '21 seconds'
#     }, 
#     {
#         'table_number': 1, 
#         'start_time': '07-15-2021 03:56:24 PM', 
#         'end_time': '07-15-2021 03:56:56 PM', 
#         'play_duration': '32 seconds'
#     }, 
#     {
#         'table_number': 4, 
#         'start_time': '07-15-2021 03:56:28 PM', 
#         'end_time': '07-15-2021 03:57:01 PM', 
#         'play_duration': '33 seconds'
#     }, 
#     {
#         'table_number': 9, 
#         'start_time': '07-15-2021 03:56:32 PM', 
#         'end_time': '07-15-2021 03:57:04 PM', 
#         'play_duration': '32 seconds'
#     }, 
#     {
#         'table_number': 10, 
#         'start_time': '07-15-2021 03:56:13 PM', 
#         'end_time': '07-15-2021 03:57:10 PM', 
#         'play_duration': '57 seconds'
#     }
# ]

# Adding JSON read logic to test:

with open("pool_tables_activity.json") as file:
    pool_tables = json.load(file)

for table in pool_tables:
    print(table)