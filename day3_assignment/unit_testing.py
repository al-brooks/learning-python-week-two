import unittest # importing unit test framework

from classes import PoolTable
from datetime import datetime

class PoolTableAppTests(unittest.TestCase):

    def setUp(self):
        self.pool_table = PoolTable(1)

    # Testing if datetimes can be set to None
    def test_class_attr(self):
        self.pool_table.start_time = datetime.now()
        result = self.pool_table
        self.assertIsNotNone(result.start_time)

    def test_is_occupy_status(self):
        self.pool_table.is_occupied = True
        result = "Occupied"
        
        self.assertEqual(result, self.pool_table.occupy_status())
        # takes True or False, and returns "Not Occupied" or "Occupied"

    def test_not_occupy_status(self):
        self.pool_table.is_occupied = False
        result = "Not Occupied"
        
        self.assertEqual(result, self.pool_table.occupy_status())
        # takes True or False, and returns "Not Occupied" or "Occupied"


    def test_check_out(self):
        self.pool_table.is_occupied = False

        is_occupied_res = True
        start_time_res = datetime.now()
        start_display_res = start_time_res.strftime("%m-%d-%Y %I:%M:%S %p")

        self.pool_table.check_out()

        self.assertEqual(is_occupied_res, self.pool_table.is_occupied)
        self.assertEqual(start_display_res, self.pool_table.start_time_display)

    # Test attributes and error messages getting thrown up
    # ex. after check_out can a table be checked out again?
        

unittest.main() # run tests