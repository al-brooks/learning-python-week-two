import unittest # importing unit test framework

from classes import PoolTable

class PoolTableAppTests(unittest.TestCase):

    def setUp(self):
        self.pool_table = PoolTable(1)

unittest.main() # run tests