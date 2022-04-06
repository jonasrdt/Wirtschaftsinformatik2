# Der Nutzer soll eine Zahl eingeben können
# und das Programm gibt aus, wie viele
# Tage der jeweilige Monat hat

# Definition der Monate
januar = 31
februar = 28
maerz = 31
april = 30
mai = 31
juni = 30
juli = 31
august = 31
september = 30
oktober = 31
november = 30
dezember = 31

# Nutzereingabe abfragen
monat = int(input("Bitte geben Sie einen Monat ein (1-12): "))

if (monat == 1):
    print("Der Monat Januar hat:", januar, "Tage.")
elif(monat == 2):
    print("Der Monat Februar hat:", februar, "Tage.")
elif(monat == 3):
    print("Der Monat März hat:", maerz, "Tage.")
elif(monat == 4):
    print("Der Monat April hat:", april, "Tage.")
elif(monat == 5):
    print("Der Monat Mai hat:", mai, "Tage.")
elif(monat == 6):
    print("Der Monat Juni hat:", juni, "Tage.")
elif(monat == 7):
    print("Der Monat Juli hat:", juli, "Tage.")
elif(monat == 8):
    print("Der Monat August hat:", august, "Tage.")
elif(monat == 9):
    print("Der Monat September hat:", september, "Tage.")
elif(monat == 10):
    print("Der Monat Oktober hat:", oktober, "Tage.")
elif(monat == 11):
    print("Der Monat November hat:", november, "Tage.")
elif(monat == 12):
    print("Der Monat Dezember hat:", dezember, "Tage.")
else:
    print("Es wurde kein passender Monat gefunden.")
