# Entwickeln Sie mit Python eine Funktion, die bei Übergabe
# einer natürlichen Zahl n das Produkt 1*2*...*n berechnet und zurückgibt.

def zahleneingabe():
    korrekte_eingabe = False
    while not korrekte_eingabe:
        try:
            zahl = int(input("Bitte geben Sie eine natürlich Zahl ein: "))
            korrekte_eingabe = True
        except:
            print("Bitte geben Sie nur natürliche Zahlen ein.")
    return zahl

def fakultaet(natuerliche_zahl):
    # Zählt von 1 bis zur eingegeben Zahl +1 in Schrittweite 1
    for zaehler in range(1,natuerliche_zahl):
        natuerliche_zahl = natuerliche_zahl * zaehler
    return natuerliche_zahl

natuerliche_zahl = zahleneingabe()
fakultaet = fakultaet(natuerliche_zahl)

print("Die Fakultät von", natuerliche_zahl, "lautet", fakultaet, ".")