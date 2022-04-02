import sys
sys.path.append('..')
import unittest
from Battery.spindlerBattery import SpindlerBattery
# import SpindlerBattery
from datetime import datetime

class TestSpindlerBatter(unittest.TestCase):
    def test_service_true(self):
        today = datetime.today().date()
        last_date = today.replace(year = today.year - 3)
        battery = SpindlerBattery(last_date,today)
        self.assertTrue(battery.needs_service())

    def test_service_false(self):
        today = datetime.today().date()
        last_date = today.replace(year = today.year - 1)
        battery = SpindlerBattery(last_date,today)
        
        self.assertFalse(battery.needs_service())

if __name__ == '__main__':
    unittest.main()