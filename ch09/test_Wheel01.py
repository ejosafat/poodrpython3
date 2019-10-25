from unittest import TestCase
from sources.Wheel01 import Wheel


class WheelTest(TestCase):
    def test_calculates_diameter(self):
        wheel = Wheel(26, 1.5)
        self.assertAlmostEqual(29, wheel.diameter, delta=0.01)
