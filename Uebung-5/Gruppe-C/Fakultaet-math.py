# Entwickeln Sie mit Python eine Funktion, die bei Übergabe einer natürlichen
# Zahl n das Produkt 1*2*...*n berechnet und zurückgibt.

# Importieren des Packages Math
import math

# Festlegen der Abbruchbedingung
richtige_eingabe = False

# While Schleife solange, bis ganze Zahl eingegeben wurde
while not richtige_eingabe:
    try:
        ganze_zahl = int(input("Bitte geben Sie eine ganze Zahl ein: "))
        richtige_eingabe = True
    except:
        print("Bitte geben Sie nur ganze Zahlen ein.")
    
# Berechnen der Fakultät
print("Die Fakultät von", ganze_zahl, "beträgt:", math.factorial(ganze_zahl))
