
class TimeRange:
    def __init__(self, start, end):
        self.start = start
        self.end = end

    def __hash__(self, other):

    def __eq__(self, other):
        return self.start == other.start and \
               self.end == other.end
