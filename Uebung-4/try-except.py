
falsche_eingabe = True

# Schleife die solange läuft, bis das Alter korrekt eingegeben wurde
while falsche_eingabe:
    # Try/Except, um etwaige Fehleingaben abzufangen
    try:
        # Nutzer um Eingabe des Alters bitten
        alter = int(input("Bitte geben Sie Ihr Geburtsjahr ein: "))
        print("Ihr Geburtsjahr ist", alter)
        # Inhaltliche Prüfung des Alters
        if alter > 2003 and alter < 1910:
            print("Du bist leider zu jung/alt, um diese Seite zu besuchen.")
        else:
            print("Willkommen auf der Seite von Carlsberg Deutschland")
            # Abbruchbedingung erfüllen, sobald richtie Eingabe erfolgt
            falsche_eingabe = False
    except:
        print("Das war keine gültige Eingabe.")
