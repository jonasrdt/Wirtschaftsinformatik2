# Entwickeln Sie mit Python eine Funktion, die bei Übergabe
# einer natürlichen Zahl n das Produkt 1*2*...*n berechnet und zurückgibt.

# 5!
# 1 * 2 * 3 * 4 * 5

# Funktion zur Berechnung der Fakultät definieren
def fakultaet(natuerliche_zahl):
    berechneter_wert = 1
    for zaehler in range(1,natuerliche_zahl+1):
        berechneter_wert = berechneter_wert * zaehler
    return berechneter_wert

gueltige_eingabe = False
while not gueltige_eingabe:
    try:
        ganze_zahl = int(input("Bitte geben Sie eine natürliche Zahl ein: "))
        print("Die von Ihnen eingegeben Zahl lautet:", ganze_zahl)
        gueltige_eingabe = True
    except:
        print("Bitte geben Sie nur Zahlen ein.")

print("Die Fakultät von", ganze_zahl, "lautet", fakultaet(ganze_zahl))
