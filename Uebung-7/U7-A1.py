# Erstellen Sie ein Python-Programm das solange eine natürliche Zahl einliest,
# bis keine Zahl oder eine falsche Eingabe erfolgt.
# Am Ende soll die größte Zahl von den eingegebenen
# Zahlen auf der Konsole ausgegeben werden.

# Instanziieren der Variable 'eingebene_zahlen' vom Datentyp liste
eingegebene_zahlen = []

# Abbruchbedingung 'korrekte_eingabe'
korrekte_eingabe = True
while korrekte_eingabe:
    # Technische Fehlerabfrage
    try:
        zahl = int(input("Geben Sie eine Zahl ein: "))
        # Hinzufügen der 'zahl' zu der Liste 'eingegebene_zahlen'
        eingegebene_zahlen.append(zahl)
        print("Aktuell lautet die größte Zahl:", max(eingegebene_zahlen))
    except:
        print("Sie haben keine Zahl eingegeben. Die Eingabe wird jetzt abgebrochen")
        korrekte_eingabe = False

# Ermitteln der größten Zahl
groesste_zahl = max(eingegebene_zahlen)
print("Die größte Zahl lautet:", groesste_zahl)
