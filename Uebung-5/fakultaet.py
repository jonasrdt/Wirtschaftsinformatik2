# Entwickeln Sie mit Python eine Funktion, die bei Übergabe einer
# natürlichen Zahl n das Produkt 1*2*...*n berechnet und zurückgibt.

# Variablendefinition
fakultaet = 1

# Datentyp Integer
korrekte_eingaben = False
while not korrekte_eingaben:
    try:
        zahl = int(input("Bitte geben Sie eine natürliche Zahl ein: "))
        korrekte_eingaben = True
    except:
        print("Bitte geben Sie nur natürliche Zahlen ein.")

# Schleife für Durchläufe zur Berechnung der Fakultät
for zaehler in range(1, zahl+1):
    # Die Variable Fakultät wird in jedem Durchlauf mit dem Zähler multipliziert
    fakultaet = fakultaet * zaehler
    print("Der aktuelle Wert beträgt:", fakultaet)
