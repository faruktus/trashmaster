import locale, datetime
locale.setlocale(locale.LC_ALL, 'de_DE.utf8')
from datetime import date, datetime
from dateutil.relativedelta import relativedelta
import calendar


heute = date.today()

curr_month=datetime.now().month
curr_year=datetime.now().year
curr_day=datetime.now().day
#days_curr_month=calendar.monthrange(2025, curr_month)[1]
days_curr_month=7

inter=3

if inter > 1:
    div = round(days_curr_month/(inter))
    listi=[]
else:
    listi=[15]
    inter=0

cnt=1
for x in range(inter):
    listi.append(cnt)
    cnt+=div-1

print(listi)

listi=[datetime(curr_year, curr_month, x).strftime("%d, %m, %Y") for x in sorted(listi)]
print(listi)








    







    

#print(Geburtstag.strftime("%d.%m.%Y"))

#print(deimuada.days)

delta=relativedelta(months=+1)

Geburtstag = date(2025, 3, 28)
