from functools import total_ordering
from collections.abc import Set, Container

@total_ordering
class Datetime:
    def __init__(self, *args):
        if len(args) == 1:
            date = args[0]
            self.hour = date.hour
            self.minute = date.minute
        elif len(args) == 2:
            hour, minute = args
            self.hour = hour
            self.minute = minute

    def __eq__(self, other):
        return self.hour == other.hour and \
              self.minute == other.minute

    def __lt__(self, other):
        return self.hour < other.hour or \
               (self.hour == other.hour and self.minute < other.minute)

    def __repr__(self):
        return '{0}:{1}'.format(self.hour, self.minute)

@total_ordering
class TimeRange(Container):
    def __init__(self, start, end):
        if start > end:
            raise ValueError('start mustn\'t be greater then end')
        self.start = start
        self.end = end

    def duration(self):
        return self.end - self.begin

    def __lt__(self, other):
        return self.start < other.start or \
               (self.start == other.start and self.duration() < other.duration())

    def __eq__(self, other):
        return self.start == other.start and \
               self.end == other.end

    def __contains__(self, item):
        return self.start <= item.start and \
               self.end >= item.end

    def __repr__(self):
        return '{0}-{1}'.format(self.start, self.end)

@total_ordering
class Activity:
    def __init__(self, time_range, name):
        self.time_range = time_range
        self.name = name

    def __repr__(self):
        return '({0}, {1})'.format(self.time_range, self.name)

    def __eq__(self, other):
        return self.time_range == other.time_range

    def __lt__(self, other):
        return self.time_range < other.time_range

class Syllabus(Set):
    def __init__(self, data=[]):
        self.data = sorted(data)

    def __contains__(self, time_range):
        for acitivity in data:
            if time_range in activity.time_range:
                return True
        return False

    def __repr__(self):
        return str(self.data)

    def __iter__(self): pass

    def __len__(self):
        return len(self.data)

    def get_superset(self, item):
        for x in data: pass

    def add(self, activity):
        self.data = sorted(self.data + [activity])
