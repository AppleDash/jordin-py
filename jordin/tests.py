import unittest
from . import math

class TestMath(unittest.TestCase):
    def test_zero(self):
        self.assertEqual(math.zero(), 0)

    def test_one(self):
        self.assertEqual(math.one(), 1)

    def test_pi(self):
        self.assertAlmostEqual(math.pi(), 3, delta=1)

    def test_e(self):
        self.assertAlmostEqual(math.e(), 3, delta=1)

    def test_deg2rad(self):
        self.assertAlmostEqual(math.deg2rad(90), 1.5, delta=0.1)

    def test_rad2deg(self):
        self.assertAlmostEqual(math.rad2deg(1.5707963268), 90)
