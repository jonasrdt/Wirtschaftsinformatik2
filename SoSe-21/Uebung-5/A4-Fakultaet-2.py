# Aufgabe 4
# Entwickeln Sie mit Python eine Funktion, die bei Übergabe einer 
# natürlichen Zahl n das Produkt 1*2*...*n berechnet und zurückgibt.

# Definition der Funktion
def fakultaetBerechnen(zahl):
    print("Sie wollen die Fakultät von", zahl, "berechnen. Dies wird jetzt durchgeführt.")
    fakultaet = 1
    for zaehler in range(zahl, 0, -1):
        fakultaet = fakultaet * zaehler
    return fakultaet

korrekte_eingabe = False
while not korrekte_eingabe:
    try: 
        zahl = int(input("Bitte geben Sie eine natürlich Zahl ein: "))
        korrekte_eingabe = True
    except:
        print("Bitte geben Sie nur Zahlen ein.")

print("Die Fakultät von", zahl, "beträgt", fakultaetBerechnen(zahl))