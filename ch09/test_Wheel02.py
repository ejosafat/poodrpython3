from unittest import TestCase
from sources.Wheel01 import Wheel


class WheelTest(TestCase):
    def setUp(self):
        self.wheel = Wheel(26, 1.5)

    def test_implements_the_diameterizable_interface(self):
        self.assertTrue('diameter' in dir(self.wheel))

    def test_calculates_diameter(self):
        self.assertAlmostEqual(29, self.wheel.diameter, delta=0.01)
