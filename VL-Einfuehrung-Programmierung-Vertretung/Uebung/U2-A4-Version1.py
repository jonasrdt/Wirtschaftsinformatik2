# Erstellen Sie ein Python-Programm, das für ein eingegebenes beliebiges
# Datum die Anzahl der bisher im Jahr vergangenen Tage ausgibt.
# (Der Einfachheit halber soll davon ausgegeben werden, dass der Februar immer 28 Tage hat.)

jan = 31
feb = 28
mrz = 31
april = 30
mai = 31
jun = 30
jul = 31
aug = 31
sept = 30
okt = 31
nov = 30
dez = 31

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


if monate == 1:
    print(f"Tage seit Jahresanfang {tage}")
elif monate == 2:
    vergangene_tage = tage + jan
    print(f"Tage seit Jahresanfang {vergangene_tage}")
elif monate == 3:
    vergangene_tage = tage + jan + feb
    print(f"Tage seit Jahresanfang {vergangene_tage}")
elif monate == 4:
    vergangene_tage = tage + jan + feb + mrz
    print(f"Tage seit Jahresanfang {vergangene_tage}")
elif monate == 5:
    vergangene_tage = tage + jan + feb + mrz + april
    print(f"Tage seit Jahresanfang {vergangene_tage}")