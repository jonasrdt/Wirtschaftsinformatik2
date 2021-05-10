 # Das ist ein Programm, um die Anzahl der Monate
 # eines durch den Nutzer eingegebenen Monats herauszufinden.

# EVA
# # E = Eingabe
# # V = Verarbeitung
# # A = Ausgabe

# while - Schleife wird solange ausgeführt, wie die verknüpfte Bedingung wahr ist
# for - Schleife wird solange ausgeführt, wie es ihr vorgegeben wurde

# Initialisieren eines Zustands für die Schleife
schleife = True

# while-Schleife mit Bedingung True
while schleife:
    # Nutzereingabe für den Monat
    monat = int(input("Bitte geben Sie einen Monat ein (1-12 für die Monate) oder -99 wenn Sie das Programm abbrechen wollen: "))
    
    # Verarbeitung für den entsprechenden Monat
    anzahl_tage = 0

    # Abbruchmechanismus zum Beenden der Schleife
    if monat == -99:
        schleife = False

    # Wiedergabe der Anzahl der Tage pro Monat in Abhängigkeit von der Nutzereingabe
    if monat == 1 or monat == 3 or monat == 5 or monat == 7 or monat == 8 or monat == 10 or monat == 12:
        anzahl_tage = 31
    elif monat == 2:
        anzahl_tage = 28
    elif monat < 1 or monat > 12:
        print("Die Eingabe kann keinem Monat zugeordnet werden. Bitte geben Sie nur Monate zwischen 1 und 12 ein.")
    else:
        anzahl_tage = 30

    # Ausgabe der Anzahl der Tage pro Monat sowie Prüfung ob Eingabe innerhalb des Intervalls liegt
    if 1 <= monat <= 12:
        print("Der Monat", monat, "hat", anzahl_tage, "Tage.")