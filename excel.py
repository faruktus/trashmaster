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
month_days = obj.itermonthdays(2025, 10)
print([x for x in month_days if x])


monthnames = [x for x in calendar.month_name if x]

header = [x for x in sheet.iter_cols(min_row=1, max_row=1, max_col=12)]
for index, row in enumerate(header):
    row[0].value = deimuada[index] 
    



wb.save("excel.xlsx")
