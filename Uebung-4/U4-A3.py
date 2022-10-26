zaehler = 9

# Läuft von 1 bis einschl. 9
for zeilen in range(1, zaehler +1):
    # Erzeugt Leerzeichen in Abhängigkeit von der Anzahl der Zeilen. Erste Zeile = Viele Leerzeichen und so weiter …
    for leerzeichen in range(zaehler-zeilen):
        print(" ", end=" ")
    # Gibt aufwärtszählend so viele Zahlen aus, wie Zeilen vorhanden sind
    for zahl in range(1, zeilen+1):
        print(zahl, end= " ")
    # Gibt abwärtszählend so viele Zahlen aus, wie Zeilen vorhanden sind
    for zahl_2 in range(zeilen-1, 0, -1):
        print(zahl_2, end= " ")
    # Zeilenumbruch am Ende
    print()