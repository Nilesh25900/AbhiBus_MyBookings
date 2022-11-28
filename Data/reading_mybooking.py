import xlrd
from Library.config import config

def read_locators():
    workbook = xlrd.open_workbook(config.Data_Path)
    worksheet = workbook.sheet_by_name('mybooking')
    rows = worksheet.nrows
    d = {}

    for i in range(rows):
        row = worksheet.row_values(i)
        d[row[0]] = (row[1], row[2])
    return d



def read_data():
    workbook = xlrd.open_workbook(config.Data_Path)
    worksheet = workbook.sheet_by_name('Details_')
    rows = worksheet.get_rows()
    header = next(rows)
    columns = worksheet.ncols
    list1 = []
    for i in rows:
        values = ()
        for j in range(columns):
            values +=(i[j].value,)
        list1.append(values)
    return list1

# print(read_data())
# print(read_locators())