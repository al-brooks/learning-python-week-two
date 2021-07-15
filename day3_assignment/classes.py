# Step 3: Work on Classes
# ==============================================================================
from datetime import datetime

class PoolTable():

    def __init__(self, number):
        self.number = number
        self.is_occupied = False
        self.start_time = None
        self.start_time_display = None
        self.end_time = None
        self.end_time_display = None
        self.play_duraton = None
        self.play_duraton_display = None

    def occupy_status(self):
        if self.is_occupied == False:
            return "Not Occupied"
        else:
            return "Occupied"

    def check_out(self):
        if self.is_occupied == False:
            self.is_occupied = True
            self.start_time = datetime.now()
            self.start_time_display = self.start_time.strftime("%m-%d-%Y %I:%M:%S %p")
        else:
            print("This table is occupied, choose another")

    def duration_display(self):
        duration_secs = self.play_duraton.total_seconds()
        duration_min = duration_secs / 60
        duration_hour = duration_min / 60

        if duration_min < 1:
            return "%.0f seconds" % duration_secs
        elif duration_min >= 1 and duration_min < 60:
            return "%.1f minutes" % duration_min
        else:
            return "%.2f hours" % duration_hour

    def session_cost(self):
        duration_secs = self.play_duraton.total_seconds()
        duration_min = duration_secs / 60

        if duration_min < 1:
            return 0
        else:
            return "%.2f" % (duration_min * 0.50) # based on $30 an hour cost


    def check_in_to_dict(self):
        duration = self.duration_display()
        cost = self.session_cost()
        pt_dict = {
            "table_number": self.number,
            "start_time": self.start_time_display,
            "end_time": self.end_time_display,
            "play_duration": duration,
            "session_cost": cost
            }
        return pt_dict
        
    def check_in(self):
        self.end_time = datetime.now()
        self.end_time_display = self.end_time.strftime("%m-%d-%Y %I:%M:%S %p")
        self.play_duraton = self.end_time - self.start_time

        print("\tThanks for using our service:")
        print("\t==========================================")
        print(f"\tStart Time - {self.start_time_display}")
        print(f"\tEnd Time - {self.end_time_display}")
        print(f"\tYour session duration was approximately: {self.duration_display()}")
        print(f"\tYour session cost was approximately: ${self.session_cost()}\n")

        # Testing dictionary method
        # print(self.check_in_to_dict())

    def attribute_reset(self):        
        # Resetting attributes
        self.is_occupied = False
        self.start_time = None
        self.start_time_display = None
        self.end_time = None
        self.end_time_display = None

    