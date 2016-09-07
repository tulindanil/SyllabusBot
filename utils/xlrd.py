import xlrd

FILE_PATH = 'syllabus.xlsx'

book = xlrd.open_workbook(FILE_PATH)
sh = book.sheet_by_index(0)
print("{0} {1} {2}".format(sh.name, sh.nrows, sh.ncols))
print(sh.cell_value(rowx=1, colx=1))
for rx in range(sh.nrows):
    print(sh.row(rx))
