
# Festlegen der Abbruchbedingung
richtige_angabe = False

# while Schleife die solange läuft, bis der Nutzer eine Zahl eingegeben hat
while not richtige_angabe:
    try:
        einkommen = float(input("Bitte geben Sie Ihr monatl. Bruttoeinkommen ein: "))
        print("Ihr monatliches Bruttoeinkommen beträgt", einkommen, "€.")
        richtige_angabe = True
    except:
        print("Bitte geben Sie nur Zahlen ein.")
