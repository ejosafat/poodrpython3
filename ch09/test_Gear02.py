from unittest import TestCase
from sources.Gear02 import Gear


class DiameterDouble:
    @property
    def diameter(self):
        return 10


class GearTest(TestCase):
    def test_calculates_gear_inches(self):
        gear = Gear(chainring=52, cog=11, wheel=DiameterDouble())
        self.assertAlmostEqual(47.27, gear.gear_inches, delta=0.01)
