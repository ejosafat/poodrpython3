class Schedule:
    def is_scheduled(self, schedulable, start_date, end_date):
        print('This %s is not scheduled' % schedulable.__class__)
        print('between %s and %s' % (start_date, end_date))
