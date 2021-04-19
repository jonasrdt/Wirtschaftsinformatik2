# while-Schleife
# for-Schleife
# Schleifen solange, bis die Abbruchbedingung erfüllt ist

# Ermittlung der Anzahl der Tage für einen bestimmten Monat (1-12)
# EVA
## E = Eingabe
## V = Verarbeitung
## A = Ausgabe
# int = ganzzahlige Werte
# float = Dezimalzahlen

# Intialisieren einen Zustand für die Schleife
schleife = True

while schleife:
    # Eingabe vom Nutzer
    monat = int(input("Bitten geben Sie einen Monat ein (1-12 für die Monate) oder -99 wenn Sie abbrechen wollen:"))

    # Verarbeitung für den entsprechenden Monat
    anzahl_tage = 0

    # Abbruchmechanismus
    if monat == -99:
        schleife = False

    # Abprüfen der Monate und festlegen der entsprechenden Tage
    if monat == 1 or monat == 3 or monat == 5 or monat == 7 or monat == 8 or monat == 10 or monat == 12:
        anzahl_tage = 31
    elif monat == 2:
        anzahl_tage = 28
    elif monat < 1 or monat > 12:
        print("Bitte nur Zahlen von 1-12 eingeben.")
    else:
        anzahl_tage = 30

    if monat >= 1 and monat <= 12:
        print ("Der Monat", monat, "hat", anzahl_tage, "Tage.")