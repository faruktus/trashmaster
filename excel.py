import openpyxl
import locale
locale.setlocale(locale.LC_ALL, 'de_DE.utf8')
from openpyxl import Workbook
import calendar
from calendar import Calendar, TextCalendar
from jason import dict_days, starting_date
from dateutil.relativedelta import relativedelta

wb = Workbook()
sheet = wb.active

sheet.title = "Data"

starting_year = int(starting_date.strftime("%Y"))
starting_month = int(starting_date.strftime("%m"))

monthnames = []
for x in range(1,13):
    monthnames.append(starting_date.strftime("%B %y"))
    starting_date += relativedelta(months=1)

obj=Calendar()
dict_month={}
for index, x in enumerate(monthnames):
    dict_month[x] = [x for x in obj.itermonthdays(starting_year, 
                                                 ((index + starting_month-1)%12)+1) if x]

col = [x for x in range(1, 24, 2)]
for i, (k, v) in enumerate(dict_month.items()):
    sheet.cell(row=1, column=col[i], value=k)
    #sheet.merge_cells(start_column = col[i], end_column = col[i]+1, start_row=1, end_row=1)
    row = 2
    for day in v:
        sheet.cell(row=row, column=col[i], value=day)
        row += 1

    


header = list(sheet.iter_cols(min_row=1, max_row=1, max_col=12))
#print(header)

"""
sheet["A1"] = "Jänner"
sheet["B1"] = "deivoda"
sheet["C1"] = "bamoida"

data = [["Alice", 25, "Nwq sodif"], ["Bob", 26, "lsdkjfl"], ["Charlie", 234, "csdf"]]

for row_idx, row_data in enumerate(data, start=2):
    for col_idx, cell_value in enumerate(row_data, start=1):
        sheet.cell(row=row_idx, column=col_idx, value=cell_value)
listi=[]
for index, row in enumerate(header):
    row[0].value = monthnames[index] 
"""

wb.save("excel.xlsx")
