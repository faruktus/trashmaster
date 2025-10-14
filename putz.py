import locale, datetime
locale.setlocale(locale.LC_ALL, 'de_DE.utf8')
from datetime import date, datetime 
from dateutil.relativedelta import relativedelta
import time
import json

Bereiche = ["Vorraum", "Garderobe", "WC"]

year = 2025
month = 3
day = 1

starting_date=datetime(year, month, day)
plusyear = starting_date + relativedelta(years=1)


dicti={}
for x in Bereiche:
    eingabe = input(x + "Woche, Monat, Jahr: ")
    inter = int(input("Intervall: "))

    if eingabe == "Woche":
        calc = round(365/53/inter)
    if eingabe == "Monat":
        calc = round(365/12/inter)
    if eingabe == "Jahr":
        calc = round(365/inter)

    listi=[]
    new_start = starting_date
    while starting_date < plusyear:
        starting_date += relativedelta(days=calc)
        listi.append(starting_date.strftime("%d, %m, %Y"))
    dicti[x] = listi
    starting_date=new_start

with open("deimuada.json", mode="w", encoding="utf-8") as write_file:
    json.dump(dicti, write_file, indent=2)

        

    










"""
def find_first(year, month):
    d = datetime(year, int(month), 7)
    offset = -d.weekday()
    print(offset)
    return d + timedelta(offset)

print(find_first(2025, 1))
heute = date.today()
curr_month=datetime.now().month
curr_year=datetime.now().year
curr_week=datetime.now().isocalendar()[1]
print(first_Monday.isocalender[1])
#days_curr_month=calendar.monthrange(2025, curr_month)[1]

#print(hola.strftime("%d, %m, %Y, %A"))
cnt+=timedelta(days=div)
listi=[x.strftime("%d, %m, %Y") for x in sorted(listi)]
"""
    







    

#print(Geburtstag.strftime("%d.%m.%Y"))

#print(deimuada.days)

