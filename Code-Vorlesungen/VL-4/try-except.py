
# Festlegen der Abbruchbedingung
ungueltige_eingabe = True

# Starten der While-Schleife
while ungueltige_eingabe:
    # Versuche Nutzereingabe zu erhalten
    try:
        alter = int(input("Bitte geben Sie Ihr Alter ein: "))
        if alter >= 18:
            print("Dein Alter ist", alter, ".")
            ungueltige_eingabe = False
        else:
            print("Du bist leider nicht alt genug.")
    # Sollte Nutzereingabe nicht int sein, gibt folgende exception aus
    except:
        print("Bitte geben Sie nur ganze Zahlen ein.")

