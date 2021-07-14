from datetime import datetime

# Testing duration display

time1 = datetime.now()
time2 = datetime(2021,7,15,0,0,0,0)
duration = time2 - time1


duration_secs = duration.total_seconds()
duration_min = duration_secs / 60
duration_hour = duration_min / 60

print("%.0f" % duration_secs)
print("%.2f" % duration_min)
print("%.2f" % duration_hour)


# if duration_min < 1:
#     return duration_secs
# elif duration_min >= 1 and duration_min < 60:
#     return duration_min
# elif duration_min > 60:
#     return duration_hour
# else:
#     print("bad code")