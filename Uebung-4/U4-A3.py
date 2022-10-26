zaehler = 9

# Läuft von 1 bis einschl. 9
for zeilen in range(1, zaehler +1):
    for leerzeichen in range(zaehler-zeilen):
        print(" ", end=" ")
    # Läuft von 1 bis einschl. den Wert von Zahlen
    for zahl in range(1, zeilen+1):
        print(zahl, end= " ")
    for zahl_2 in range(zeilen-1, 0, -1):
        print(zahl_2, end= " ")
    print()