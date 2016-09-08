import sys
import xlrd

from storage import Storage as S

from syllabus import Syllabus
from syllabus import TimeRange as T
from syllabus import Activity as A
from syllabus import Datetime as D

file_path = sys.argv[1]

book = xlrd.open_workbook(file_path)
sh = book.sheet_by_index(0)

s = S()
syllabuses = []

def datetime(number):
    return D(int(number / 100), number % 100)

def make_range(time):
    numbers = [int(s) for s in time.split() if s.isdigit()]
    datetimes = [datetime(x) for x in numbers]
    return T(datetimes[0], datetimes[1])

def activity(time, subject):
    time_range = make_range(time)
    subject_name = subject
    return A(time_range, subject_name)

for rx in range(sh.nrows):
    time, subject = sh.row(rx)
    if subject.ctype == 0 and '-' not in time.value:
        # new weekday
        s.update_day(time.value, syllabuses)
        syllabuses.append(Syllabus([]))
    elif subject.ctype == 1:
        # that's an subject
        syllabus = syllabuses[-1]
        a = activity(time.value, subject.value)
        print(a)
        syllabus.add(a)
