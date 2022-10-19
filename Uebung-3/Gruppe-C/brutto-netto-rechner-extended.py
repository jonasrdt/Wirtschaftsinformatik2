# Definieren der Abbruchbedingung
korrekte_eingabe = False
# Starten der while-Schleife, solange noch KEINE korrekte Eingabe getätigt wurde
while not korrekte_eingabe:
    # Abfragen des Familienstands des Users
    familienstand = input("Bitte geben Sie Ihren Familienstand an: ")
    print("Der von Ihnen eingegeben Familienstand ist:", familienstand)
    # Prüfen, ob der familienstand == "ledig" ist 
    if familienstand.lower() == "ledig":
        print("Sie haben angegeben, dass Sie ledig sind.")
        # Setzen der Abbruchbedingung, da eine korrekte Eingabe getätigt wurde
        korrekte_eingabe = True
    # Prüfen, ob der familienstand == "verheiratet" ist 
    elif familienstand.lower() == "verheiratet":
        print("Sie haben angegeben, dass Sie verheiratet sind.")
        # Setzen der Abbruchbedingung, da eine korrekte Eingabe getätigt wurde
        korrekte_eingabe = True
    # Wenn nichts von den vorherigen zutrifft, soll zu einer neuen Eingabe aufgefordert werden.
    else:
        print("Sie scheinen weder verheiratet noch ledig zu sein. Überprüfen Sie Ihre Eingabe.")

# Definieren der Abbruchbedingung
korrektes_bruttogehalt = False
# Starten der while-Schleife, solange noch KEINE korrekte Eingabe des Bruttogehalts getätigt wurde
while not korrektes_bruttogehalt:
    # Erfassen der Eingabe des Users
    bruttogehalt = int(input("Bitte geben Sie Ihr monatliches Bruttogehalt ein: "))
    # Prüfen, ob das Bruttogehalt größer oder gleich 0 ist
    if bruttogehalt >= 0:
        # Setzen der Abbruchvariable
        korrektes_bruttogehalt = True
        # Hinweis auf Einkommenssteuerfreibetrag
        if bruttogehalt < 886:
            print("Ihr Bruttogehalt i.H.v.", bruttogehalt, "liegt unter dem Freibetrag. Daher fallen keine Steuern an.")
    else:
        # Ausführen, wenn eine Zahl kleiner als 0 eingegeben wurde
        print("Bitte geben Sie ein korrektes Bruttogehalt, größer als 0.00€ an.")
