

def multiply(zahl_1, zahl_2):
    ergebnis = zahl_1 * zahl_2
    # Return macht den Wert hinter der Variable 'ergebnis'
    # nach außen, also in den globalen Kontext, verfügbar.
    return ergebnis
    
print(multiply(5,3))