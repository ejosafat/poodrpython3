from datetime import date
from Schedulable01 import SchedulableMixin


class Bicycle(SchedulableMixin):
    @property
    def lead_days(self):
        return 1

starting = date(2015, 9, 4)
ending = date(2015, 9, 10)

b = Bicycle()
print(b.is_schedulable(starting, ending))
