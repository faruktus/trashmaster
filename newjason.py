import json
from datetime import datetime, date
from dateutil.relativedelta import relativedelta
from dateutil.rrule import *
from dateutil.parser import *
from itertools import count

try:
    with open("deimuada.json", mode="r", encoding="utf-8") as read_file:
           dict_interval = json.load(read_file)
except:
    print("no file")

#print(dict_interval)
#print()

starting_date = date.today()
plusyear = starting_date + relativedelta(months=11)

# Compare 2 Lists for duplicates
def f_CompList(firstList, secondList):
    wholeList = len(firstList) + len(secondList)
    uniqueList = len(set(firstList + secondList))
    return wholeList - uniqueList

# increase every item in list for +1 day everytime function is called (max + 6 days)
# e.g. list = [3.1.25, 4.1.25] 1st call: [4.1.25, 5.1.25] 2nd call: [5.1.25, 6.1.25]
cnt = count(1)
def f_IterList(listi):
    global cnt
    nextday = next(cnt) % 6
    return [x + relativedelta(days=nextday) for x in listi]


# compare 2 datelists - raise v_iterlist by 1 day while 0 duplicates 
#                       OR return list with least duplicates
def f_CompMultilist(v_iterlist, list2):
    templist = []
    for x in range(6):
        iterlist = f_IterList(v_iterlist)
        complist = f_CompList(iterlist, list2)
        if complist == 0:
            return iterlist
        else:
            templist.append([complist, iterlist])
    return sorted(templist)[0][1]

# dict_days: BEREICH = [Liste von errechneten Tagen im Format datetime.date für 1 Jahr]
dict_days={}
try:
    global calc
    for k,v in dict_interval.items():
        if v[0] == "Woche":
          calc = int(334/47/v[1])
        if v[0]  == "Monat":
          calc = int(334/11/v[1])
        if v[0]  == "Jahr":
          calc = int(334/v[1])

        date_list=[]
        new_start = starting_date
        while starting_date <= (plusyear-relativedelta(days=calc)):
            starting_date += relativedelta(days=calc)
            #print(starting_date)
            date_list.append(starting_date)
            #listi.append(starting_date.strftime("%d, %m, %Y"))
            dict_days[k] = date_list
        #print()

        # clear duplicates
        #dict_values = [y for x in dict_days.values() for y in x]
        #dict_days[k] = f_CompMultilist(date_list, dict_values)

        starting_date=new_start   
except:
    print("not enough/wrong data")

#print(dict_days)
listi = [y for x in dict_days.values() for y in x]
#print(len(listi))
#print(len(set(listi)))


garderobe = [date(2025, 11, 5), date(2025, 11, 6), date(2025, 11, 7)]
vorraum = [date(2025, 11, 4), date(2025, 11, 5), date(2025, 11, 6), date(2025, 12, 3)]

xx=date(2025,11,5)



#print(xx.strftime("%B %y, %d"))

#print(f_CompMultilist(garderobe, deimuade))


#print(dict_days)

#print(f_CompList(dict_days["Garderobe"], dict_days["Vorraum"]))
#print(f_CompList([1,2,3], [1,2,4])[0])    

"""
comparison_list = []
temp_list = []
mod_list = []
for k, v in dict_days.items():
    if comparison_list and f_CompList(comparison_list, v)[0]:
        for index, item in enumerate(v):
            for x in range(3):
                temp_list.append(item + relativedelta(days=(x+1)%7))
        mod_list.append(temp_list)
    comparison_list += v 
#print(dict_days)
print("\n\n\n\n")
print(len([y for x in dict_days.values() for y in x]))
print(len(set([y for x in dict_days.values() for y in x])))

#print("whole: " + str(whole))
#print("seti: " + str(seti))


"""
