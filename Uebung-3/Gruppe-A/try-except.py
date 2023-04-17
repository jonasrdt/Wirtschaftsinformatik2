
korrekte_eingabe = False


while not korrekte_eingabe:
    # Technische Fehlerabfrage. Es wird geprüft, ob eine umwandelbare Zahl eingegeben wurde
    try:
        alter = int(input("Bitte geben Sie Ihr Alter ein: "))
        # Inhaltliche Fehlerabfrage. Es wird geprüft, ob das Alter größer 0 ist.
        if alter > 0:
            print("Das von Ihnen eingebene Alter lautet:", alter)
            korrekte_eingabe = True
        else:
            print("Bitte geben Sie ein Alter größer 0 an.")
    except:
        print("Bitte geben Sie nur Zahlen ein: ")