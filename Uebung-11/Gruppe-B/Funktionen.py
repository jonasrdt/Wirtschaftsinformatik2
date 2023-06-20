# Schreiben Sie eine Funktion mit dem Namen 'divide()',
# welche zwei Zahlen als Parameter übergeben bekommt, diese
# dividiert und das Ergebnis mit return zurückgibt.

# Funktion mit lokalem Kontext
def divide(zahl_1, zahl_2):
    ergebnis = zahl_1 / zahl_2
    # return, damit das Ergebnis nach dem Ausführen von
    # divide() in den globalen Kontext übergeben wird
    return ergebnis

# Hauptprogramm mit globalem Kontext
ergebnis = divide(5,3)
print("Das Ergebnis lautet", ergebnis)