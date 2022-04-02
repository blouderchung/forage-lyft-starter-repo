import unittest

from Engine.capulet_engine import CapuletEngine


class TestCapuletEngine(unittest.TestCase):
    def test_service_true(self):
        engine = CapuletEngine(30001, 0)
        self.assertTrue(engine.needs_service())

    def test_service_false(self):
        current_mileage = 30000
        last_service_mileage = 0
        engine = CapuletEngine(30000, 0)
        self.assertFalse(engine.needs_service())

if __name__ == '__main__':
    unittest.main()