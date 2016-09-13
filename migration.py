import sys
import xlrd

from storage import Storage as S

from syllabus import Syllabus
from syllabus import TimeRange as T
from syllabus import Activity as A
from syllabus import Datetime as D

file_path = 'resources/syllabus.xlsx'

book = xlrd.open_workbook(file_path)
sh = book.sheet_by_index(0)

s = S()

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

weekday = ''

rx = 0
while rx in range(sh.nrows):
    weekday_cell, _ = sh.row(rx)
    weekday = weekday_cell.value
    syllabus = Syllabus()
    while True:
        rx = rx + 1
        try: time_cell, subject_cell = sh.row(rx)
        except: break
        if subject_cell.ctype == 0:
            break
        a = activity(time_cell.value, subject_cell.value)
        syllabus.add(a)
    s.update_day(weekday, syllabus)
