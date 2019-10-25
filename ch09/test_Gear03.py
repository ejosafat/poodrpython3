from unittest import TestCase
from unittest.mock import Mock

from sources.Gear03 import Gear


class GearTest(TestCase):
    def setUp(self):
        self.observer = Mock()
        self.gear = Gear(chainring=52, cog=11, observer=self.observer)

    def test_notifies_observers_when_cogs_change(self):
        self.gear.set_cog(27)
        self.observer.changed.assert_called_with(52, 27)

    def test_notifies_observers_when_chainrings_change(self):
        self.gear.set_chainring(42)
        self.observer.changed.assert_called_with(42, 11)
