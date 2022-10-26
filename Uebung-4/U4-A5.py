# Import der Library math
import math

# Festlegen einer Zahl, aus der die Wurzel gezogen wird
korrekte_eingabe = False
while not korrekte_eingabe:
    try:
        zahl = int(input("Bitte geben Sie eine ganze Zahl ein: "))
        korrekte_eingabe = True
    except:
        print("Bitte geben Sie nur ganze Zahlen ein.")

# Berechnen des Ergebnisses mittels der Methode sqrt()
# und runden auf vier Nachkommastellen
ergebnis = round(math.sqrt(zahl),4)

# Ausgeben des Ergebnisses
print("Die Wurzel aus", zahl, "lautet:", ergebnis)