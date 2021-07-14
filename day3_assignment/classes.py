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

    # Class methods: Occupied - Not Occupied
    def check_out(self):
        self.occupied = True
        self.start_time = datetime.now()
        self.start_time_display = self.start_time.strftime("%Y-%m-%d %H:%M:%S")
    
    def check_in(self):
        self.occupied = False
        self.end_time = datetime.now()
        self.end_time_display = self.end_time.strftime("%Y-%m-%d %H:%M:%S")

        start_calc = self.start_time_display
        end_calc = self.end_time_display

        convert_start = datetime.strptime(start_calc, "%Y-%m-%d %H:%M:%S")
        convert_end = datetime.strptime(end_calc, "%Y-%m-%d %H:%M:%S")

        self.play_duraton = convert_end - convert_start
        print(f"Thanks for using our service your session duration was: {self.play_duraton}")


