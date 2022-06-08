# Alles was hier passiert, ist lokal
def additionsrechner(zahl_1,zahl_2):
    # ergebnis ist eine lokale Variable
    ergebnis = zahl_1 + zahl_2
    return ergebnis

# zahl_1 und zahl_2 sind globale Variablen
zahl_1 = float(input("Bitte geben Sie die erste Zahl ein: "))
zahl_2 = float(input("Bitte geben Sie die zweite Zahl ein: "))

# ergebnis ist eine globale Variable
ergebnis = additionsrechner(zahl_1, zahl_2)
print("Das Ergebnis lautet:", ergebnis)