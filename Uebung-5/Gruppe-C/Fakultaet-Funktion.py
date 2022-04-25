# Entwickeln Sie mit Python eine Funktion, die bei Übergabe einer natürlichen
# Zahl n das Produkt 1*2*...*n berechnet und zurückgibt.

# Importieren des Packages Math
import math


############################
###### Funktionsdef. ######
############################

def fakultaet(zahl):
    return math.factorial(zahl)

def zahleneingabe():
    # Festlegen der Abbruchbedingung
    richtige_eingabe = False

    # While Schleife solange, bis ganze Zahl eingegeben wurde
    while not richtige_eingabe:
        try:
            zahl = int(input("Bitte geben Sie eine ganze Zahl ein: "))
            richtige_eingabe = True
        except:
            print("Bitte geben Sie nur ganze Zahlen ein.")
    return zahl

############################
###### Hauptprogramm ######
############################

# Abfragen einer Zahl vom User
ganze_zahl = zahleneingabe()
# Berechnen der Fakultät
print("Die Fakultät von", ganze_zahl, "beträgt:", fakultaet(ganze_zahl))
