import locale, datetime
locale.setlocale(locale.LC_ALL, 'de_DE.utf8')
from datetime import date, datetime 
from dateutil.relativedelta import relativedelta
import time
import json

Bereiche = ["Vorraum", "Garderobe", "WC", "Technikraum", "Küche", "Wohnzimmer",
            "Schlafzimmer", "Kinderzimmer", "Bad"]
dict_Bereiche = {i+1: x for i, x in enumerate(sorted(Bereiche))}

year = 2025
month = 3
day = 1

dict_interval={}
Putzintervall = {1: "Woche", 2: "Monat", 3: "Jahr"}

eingabe_Zeitrahmen = "None"
eingabe_Zeitrahmen = 0
eingabe_Intervall = 0
while True:
    print(dict_Bereiche)
    auswahl_Bereich = input("Choose: ")
    if auswahl_Bereich == "aus":
        break
    try:
        var = int(auswahl_Bereich)
        auswahl_Bereich = dict_Bereiche[var]
        if auswahl_Bereich == "aus":
            break
    except ValueError:
        print("no Integer")
        continue
    except KeyError:
        print("not in Keys")
        continue

    print(Putzintervall)
    eingabe_Zeitrahmen = input(auswahl_Bereich + ": ")
    if eingabe_Zeitrahmen == "aus":
        break
    try:
        var = int(eingabe_Zeitrahmen)
        eingabe_Zeitrahmen = Putzintervall[var]
    except ValueError:
        print("no Integer")
        continue
    except KeyError:
        print("not in Keys")
        continue

    print()
    eingabe_Intervall = input("Wie oft pro " + eingabe_Zeitrahmen + " soll geputzt werden: ")
    if eingabe_Intervall == "aus":
        break
    try:
        eingabe_Intervall = int(eingabe_Intervall)
    except:
        print("no Integer")

    dict_interval[auswahl_Bereich]= [eingabe_Zeitrahmen, eingabe_Intervall]
    print(dict_interval)
        
with open("deimuada.json", mode="w", encoding="utf-8") as write_file:
    json.dump(dict_interval, write_file, indent=2)

print(dict_interval)
#dict_interval = {'Garderobe': ['Woche', 1], 'Vorraum': ['Monat', 1], 'WC': ['Jahr', 3]}

starting_date=datetime(year, month, day)
plusyear = starting_date + relativedelta(years=1)

"""
dict_days={}
global calc
for k,v in dict_interval.items():
    if v[0] == "Woche":
        calc = round(365/53/v[1])
    if v[0]  == "Monat":
        calc = round(365/12/v[1])
    if v[0]  == "Jahr":
        calc = round(365/v[1])

    listi=[]
    new_start = starting_date
    while starting_date <= plusyear:
        starting_date += relativedelta(days=calc)
        listi.append(starting_date.strftime("%d, %m, %Y"))
        dict_days[k] = listi
    starting_date=new_start

print(dict_days)

with open("deimuada.json", mode="w", encoding="utf-8") as write_file:
    json.dump(dicti, write_file, indent=2)
        

    










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

