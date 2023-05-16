# Entwickeln Sie mit Python eine Funktion, die bei Übergabe einer natürlichen Zahl
# n das Produkt 1*2*...*n berechnet und zurückgibt.


### Funktionsdefinition ###
def fakultaet(natuerliche_zahl):
    # natuerliche_zahl ist hier eine lokale Variable
    for zaehler in range(1,natuerliche_zahl):
        natuerliche_zahl = natuerliche_zahl * zaehler
    return natuerliche_zahl


### Hauptprogramm ###
korrekte_eingabe = False
while not korrekte_eingabe:
    try:
        # zahl ist hier eine globale Variable
        zahl = int(input("Bitte geben Sie eine natürliche Zahl ein: "))
        korrekte_eingabe = True
    except:
        print("Bitte nur natürliche Zahlen eingeben.")

fakultaet = fakultaet(zahl)
print("Die Fakultät von", zahl, "lautet", fakultaet, ".")
