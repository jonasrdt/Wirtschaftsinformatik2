# Erstellen Sie ein Python-Programm, das für ein eingegebenes beliebiges
# Datum die Anzahl der bisher im Jahr vergangenen Tage ausgibt.
# (Der Einfachheit halber soll davon ausgegeben werden, dass der Februar immer 28 Tage hat.)


richtiges_datum = False
while not richtiges_datum:
    try:
        tage = int(input("Bitte geben Sie die Tage ein: "))
        if tage > 31:
            print("Der Monat hat maximal 31 Tage. Bitte erneut eingeben.")
            
        monate = int(input("Bitte geben Sie die Monate ein: "))
        if monate > 12:
            print("Das Jahr hat nur 12 Monate. Bitte erneut eingeben.")
        
        if 1 <= tage <= 31 and 1 <= monate <= 12:
            print(f"Sie haben {tage} Tage und {monate} Monate angegeben.")
            richtiges_datum = True
    except:
        print("Bitte geben Sie nur ganze Zahlen ein.")

anzahl_tage_jahr = tage

for monat in range(1,monate):
    if monat == 1 or monat == 3 or monat == 5 or monat == 7 or monat == 8 or monat == 10 or monat == 12:
        anzahl_tage_jahr += 31
    elif monat == 2:
        anzahl_tage_jahr += 28
    elif monat == 4 or monat == 6 or monat == 9 or monat == 11:
        anzahl_tage_jahr += 30

print(f"Es sind {anzahl_tage_jahr} Tage in diesem Jahr seit dem {tage}.{monate}.22 vergangen.")