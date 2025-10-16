import openpyxl
import locale
locale.setlocale(locale.LC_ALL, 'de_DE.utf8')
from openpyxl import Workbook
import calendar
from calendar import Calendar, TextCalendar

wb = Workbook()
sheet = wb.active

sheet.title = "Data"

sheet["A1"] = "Jänner"
sheet["B1"] = "deivoda"
sheet["C1"] = "bamoida"

data = [["Alice", 25, "Nwq sodif"], ["Bob", 26, "lsdkjfl"], ["Charlie", 234, "csdf"]]

for row_idx, row_data in enumerate(data, start=2):
    for col_idx, cell_value in enumerate(row_data, start=1):
        sheet.cell(row=row_idx, column=col_idx, value=cell_value)

obj=Calendar()

month_days = [x for x in obj.itermonthdays(2025, 10) if x]
monthnames = [x for x in calendar.month_name if x]
dict_month={}
for index, x in enumerate(monthnames):
    dict_month[x] = [x for x in obj.itermonthdays(2025, index+1) if x]

print(dict_month)
    



header = list(sheet.iter_cols(min_row=1, max_row=1, max_col=12))
#print(header)

listi=[]
for index, row in enumerate(header):
    row[0].value = monthnames[index] 


wb.save("excel.xlsx")
