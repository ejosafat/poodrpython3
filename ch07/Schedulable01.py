from datetime import timedelta

from Schedule01 import Schedule


class SchedulableMixin:
    @property
    def schedule(self):
        try:
            return self.__schedule
        except AttributeError:
            self.__schedule = Schedule()
            return self.__schedule

    def is_schedulable(self, start_date, end_date):
        return not self.is_scheduled(
            start_date - timedelta(days=self.lead_days), end_date
        )

    def is_scheduled(self, start_date, end_date):
        return self.schedule.is_scheduled(self, start_date, end_date)

    @property
    def lead_days(self):
        return 0
