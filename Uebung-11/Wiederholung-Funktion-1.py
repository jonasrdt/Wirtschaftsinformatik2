

# Funktionsdefinition
# Parameter zahl_1 und zahl_2 leben nur im lokalen Kontext
def addition(zahl_1, zahl_2):
    return zahl_1 + zahl_2

# Funktionsaufruf im Hauptprogramm
# Globaler Variable ergebnis wird das Ergebnis aus addition() zugewiesen
ergebnis = addition(5,5)
print(ergebnis+5)