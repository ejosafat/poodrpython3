from unittest import TestCase
from sources.Wheel01 import Wheel
from test_includes.DiameterizableInterface import DiameterizableInterfaceTest


class WheelTest(TestCase, DiameterizableInterfaceTest):
    def setUp(self):
        self.wheel = Wheel(26, 1.5)

    @property
    def object_tested(self):
        return self.wheel

    def test_calculates_diameter(self):
        self.assertAlmostEqual(29, self.wheel.diameter, delta=0.01)
