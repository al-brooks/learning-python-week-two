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

    def test_check_out(self):
        result = self.pool_table.occupied
        self.assertFalse(result)

unittest.main() # run tests