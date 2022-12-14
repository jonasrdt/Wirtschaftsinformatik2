# Eine while-Schleife läuft so lange, wie die mit ihr verknüpfte Bedingung wahr ist
# Einbindung von try, except zur (Ausnahme)Behandlung von technischen Fehleingaben durch den Nutzer 
korrekte_eingabe = False
while not korrekte_eingabe:
    try:
        alter = int(input("Bitte geben Sie Ihr Alter ein: "))
        # Prüfen, ob eingegebener Inhalt logisch Sinn ergibt (Inhaltlicher Fehler)
        if 4 < alter < 100:
            print("Das von Ihnen eingegebene Alter beträgt:", alter)
            korrekte_eingabe = True
        else:
            print("Bitte geben Sie ein Alter zwischen 5 und 99 Jahren an.")
    except:
        print("Bitte geben Sie nur Zahlen ein.")