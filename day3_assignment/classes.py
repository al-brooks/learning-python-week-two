# Step 3: Work on Classes
# ==============================================================================
from datetime import datetime

class PoolTable():

    def __init__(self, number):
        self.number = number
        self.occupied = False
        self.start_time = None
        self.start_time_display = None
        self.end_time = None
        self.end_time_display = None
        self.play_duraton = None

    def display_occupy(self, number):
        if self.occupied == False:
           display = f"Pool Table {number} is NOT OCCUPIED"
        else:
            display = f"Pool Table {number} is OCCUPIED"
        return display

    # Class methods: Occupied - Not Occupied
    def check_out(self):
        self.occupied = True
        self.start_time = datetime.now()
        self.start_time_display = self.start_time.strftime("%Y-%m-%d %H:%M:%S")
    
    def check_in(self):
        self.occupied = False
        self.end_time = datetime.now()
        self.end_time_display = self.end_time.strftime("%Y-%m-%d %H:%M:%S")

        convert_start = datetime.strptime(self.start_time_display, "%Y-%m-%d %H:%M:%S")
        convert_end = datetime.strptime(self.end_time_display, "%Y-%m-%d %H:%M:%S")

        self.play_duraton = convert_end - convert_start
        print(f"Thanks for using our service your session duration was: {self.play_duraton}")

    def duration_display(self):
        duration_secs = self.play_duraton.total_seconds()
        duration_min = duration_secs / 60
        duration_hour = duration_min / 60

        if duration_min < 1:
            return "%.0f" % duration_secs
        elif duration_min >= 1 and duration_min < 60:
            return "%.2f" % duration_min
        elif duration_min > 60:
            return "%.2f" % duration_hour
        else:
            print("bad code")