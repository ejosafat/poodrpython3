from unittest import TestCase
from sources.Gear01 import Gear


class GearTest(TestCase):
    def test_calculates_gear_inches(self):
        gear = Gear(chainring=52, cog=11, rim=26, tire=1.5)
        self.assertAlmostEqual(137.1, gear.gear_inches, delta=0.01)
