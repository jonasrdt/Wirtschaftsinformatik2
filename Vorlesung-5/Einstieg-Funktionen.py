

# Definieren der Funktion trenner() mit dem Parameter anzahl
def trenner(anzahl):
    for i in range(anzahl):
        print("-", end="")
    print()

# Hauptprogramm
# Abfragen der 'anzahl'
anzahl = int(input("Bitte geben Sie eine Anzahl ein: "))
# Ausführen der Funktion trenner() mit dem Parameter 'anzahl'
trenner(anzahl)
print("Und hier kommt noch ein Trenner, aber mit 20 Zeichen")
trenner(20)