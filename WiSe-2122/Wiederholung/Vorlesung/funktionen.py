# Variablendefinition
a = 15
b = 5

# Funktionsdefinitionen
def trenner(anzahl):
    for zaehler in range(anzahl):
        print("-", end="")
    print()

def restalkohol(promille, stundenschlaf):
    abgebaut = (promille / 10) * stundenschlaf
    restalkohol = round(promille - abgebaut, 2)
    return restalkohol

def zahlenAbfrage(art_des_wertes):
    richtige_eingabe = False
    while not richtige_eingabe:
        try:
            print("Bitte geben Sie einen Wert für", art_des_wertes, "ein.")
            zahl = float(input("Eingabe: "))
            richtige_eingabe = True
            return zahl
        except:
            print("Bitte geben Sie nur Zahlen ein.")

# Hauptprogramm
# Hier wäre noch eine entsprechende Fehlerabfrage zu ergänzen
schlaf = zahlenAbfrage("Schlaf")
alkohol = zahlenAbfrage("Promille")

print("Ihr Restalkohol beträgt:", restalkohol(zahlen, schlaf))
if restalkohol(alkohol, schlaf) > 0:
    print("Bitte kein Auto fahren.")
else:
    print("Gute Fahrt.")