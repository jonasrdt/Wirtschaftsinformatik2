# try, except

falsche_eingabe = True

# While Schleife die solange läuft, bis der Nutzer eine technisch korrekte Eingabe tätig
while falsche_eingabe:
    # Versuche den Code innerhalb von "try" auszuführen
    try:
        alter = int(input("Bitte geben Sie Ihr Alter ein: "))
        if alter >= 18:
            print("Ihr Alter ist:", alter, "und somit zugelassen.")
            # Wenn das Alter als Zahl eingegeben wurde, beende die Schleife
            falsche_eingabe = False
        else:
            print("Bitte geben Sie ein ausreichendes Alter ein.")
    except:
        # Wenn das Alter nicht als Zahl eingegeben wurde, gib entsprechendes Feedback
        print("Das war leider keine gültige Eingabe. Bitte geben Sie nur Zahlen ein.")