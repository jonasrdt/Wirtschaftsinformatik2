# Funktion, die zwei Werte zahl1 und zahl2 addiert
def addierezweizahlen(zahl1,zahl2):
    ergebnis = zahl1 + zahl2
    print("Das Ergebnis lautet:", ergebnis)

ungueltige_eingabe = True

while ungueltige_eingabe:
    try:
        zahl1 = int(input("Bitte geben Sie die erste Zahl ein: "))
        zahl2 = int(input("Bitte geben Sie die zweite Zahl ein: "))
        addierezweizahlen(zahl1, zahl2)
        ungueltige_eingabe = False
    except:
        print("Bitte geben Sie nur Zahlen ein.")


