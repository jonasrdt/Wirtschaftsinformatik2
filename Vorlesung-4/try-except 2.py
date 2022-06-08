# Technische Fehler abfangen mit try,except

# Definieren der Abbruchbedingung
richtige_eingabe = False

# Starten der while-Schleife
while not richtige_eingabe:
    try:
        alter = int(input("Bitte geben Sie Ihr Alter ein: "))
        # Abbrechen der Schleife, wenn ein richtiger Wert für "alter" eingegeben wurde
        richtige_eingabe = True
    except:
        print("Bitte geben Sie nur Zahlen ein.")

print("Das eingegeben Alter lautet", alter)