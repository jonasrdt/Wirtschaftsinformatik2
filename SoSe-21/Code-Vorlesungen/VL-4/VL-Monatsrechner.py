# Ermittlung der Anzahl der Tage für einen bestimmten Monat (1-12)

# EVA
# # E = Eingabe
# # V = Verarbeitung
# # A = Ausgabe

# Inititaler Zustand für die Schleife
schleife = True

while schleife:

    # Eingabe vom Nutzer
    monat = int(input("Bitte geben Sie einen Monat ein (1-12 für die Monate, -99 für Abbruch):"))

    # Verarbeitung für den entsprechenden Monat
    anzahl_tage = 0

    # Escape Mechanismus
    if monat == -99:
        schleife = False

    if monat == 1 or monat == 3 or monat == 5 or monat == 7 or monat == 8 or monat == 10 or monat == 12:
        anzahl_tage = 31
    elif monat == 2:
        anzahl_tage = 28
    elif monat < 1 or monat > 12:
        print("Bitte nur Zahlen von 1-12 eingeben.")
    else:
        anzahl_tage = 30

    print ("Der Monat", monat, "hat", anzahl_tage, "Tage.")