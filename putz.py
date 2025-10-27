import json

with open("deimuada.json", mode="r", encoding="utf-8") as json_file:
    dict_interval = json.load(json_file)

Bereiche = ["Vorraum", "Garderobe", "WC", "Technikraum", "Küche", "Wohnzimmer",
            "Schlafzimmer", "Kinderzimmer", "Bad"]
dict_Bereiche = {i+1: x for i, x in enumerate(sorted(Bereiche))}

#dict_interval={}
Putzintervall = {1: "Woche", 2: "Monat", 3: "Jahr"}

def hyphen_line():
    length = 80
    print(length*'-')

def plus_format(text):
    textlength = len(text) + 4
    print(textlength*'+')
    print('+ ' + text + ' +')
    print(textlength*'+'+'\n')

def formated_output():
    global dict_interval, dict_Bereiche
    hyphen_line()
    print("aktueller Putzplan:\n")
    for k, v in dict_interval.items():
        print(k + ": " + str(v[1]) + "x / " + v[0]) 
    hyphen_line()
    print()
    plus_format("Welcher Bereich soll geputzt werden?")
    hyphen_line()
    print(dict_Bereiche)
    hyphen_line()

break_code = "fertig"
while True:
    formated_output()
    auswahl_Bereich = input("Treffen Sie eine Wahl (Zahl angeben): ")
    if auswahl_Bereich == break_code:
        break
    try:
        var = int(auswahl_Bereich)
        auswahl_Bereich = dict_Bereiche[var]
        if auswahl_Bereich == break_code:
            break
    except ValueError:
        print("no Integer")
        continue
    except KeyError:
        print("not in Keys")
        continue

    print()
    plus_format("Soll der Bereich >>" + auswahl_Bereich + "<< wöchentlich, monatlich oder jährlich geputzt werden?")
    print(Putzintervall)
    eingabe_Zeitrahmen = input("Treffen Sie eine Wahl (Zahl angeben): ")
    if eingabe_Zeitrahmen == break_code:
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
    plus_format("Wie oft pro " + eingabe_Zeitrahmen + " soll geputzt werden?")
    eingabe_Intervall = input("Bitte Intervall als Zahl angeben: ")
    print()
    print(80*'x')
    print("Änderungen wurden übernommen! Wenn Sie beenden wollen tippen Sie ".upper() + break_code + "!")
    print("Zum Fortfahren, wählen Sie einen neuen Bereich aus: ".upper())
    print(80*'x')
    if eingabe_Intervall == break_code:
        break
    try:
        eingabe_Intervall = int(eingabe_Intervall)
    except:
        print("no Integer")
        continue

    dict_interval[auswahl_Bereich]= [eingabe_Zeitrahmen, eingabe_Intervall]
    #print(dict_interval)
    print()
        
with open("deimuada.json", mode="w", encoding="utf-8") as write_file:
    json.dump(dict_interval, write_file, indent=2)

#print(dict_interval)
#dict_interval = {'Garderobe': ['Woche', 1], 'Vorraum': ['Monat', 1], 'WC': ['Jahr', 3]}

