from datetime import timedelta, date
from Schedule01 import Schedule


class Bicycle:
    def __init__(self, **kwargs):
        self.__schedule = kwargs.get('schedule', Schedule())

    def is_schedulable(self, start_date, end_date):
        return not self.is_scheduled(
            start_date - timedelta(days=self.lead_days), end_date
        )

    def is_scheduled(self, start_date, end_date):
        return self.schedule.is_scheduled(self, start_date, end_date)

    @property
    def schedule(self):
        return self.__schedule

    @property
    def lead_days(self):
        return 1

starting = date(2015, 9, 4)
ending = date(2015, 9, 10)

b = Bicycle()
print(b.is_schedulable(starting, ending))
