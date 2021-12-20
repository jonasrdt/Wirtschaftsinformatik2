# Entwickeln Sie ein Programm, welches eine Einkaufsliste erstellt.
# Der Nutzer soll die Möglichkeit haben, Waren und deren Menge zu der Einkaufsliste hinzuzufügen.
# Ist die Ware bereits auf der Einkaufsliste, so soll dies zuerst ausgegeben werden und gefragt werden,
# ob die Menge geändert werden soll, sofern sie unterschiedlich ist.

# Variablendefinition
einkaufsliste = {}

def zahleneingabe(text):
    falsche_eingabe = True
    while falsche_eingabe:
        try:
            zahl = int(input(text))
            falsche_eingabe = False
        except:
            print("Bitte nur ganze Zahlen eingeben.")
    return zahl

def hinzufuegen():
    # Ware zu Liste hinzufügen
    print("Auf Ihrer Einkaufsliste befindet sich: ", einkaufsliste)
    ware = input("Bitte geben Sie die Ware an, die Sie hinzufügen wollen: ")
    menge = zahleneingabe("Bitte geben Sie die Menge der Ware ein: ")
        
    # Prüfen, ob Ware auf Liste vorhanden
    try:
        if einkaufsliste[ware] > 0:
            hinzufuegen = input("Die Ware befindet sich schon auf der Liste. Soll Sie aktualisiert werden (ja/nein): ")
            if hinzufuegen.lower() == "ja":
                einkaufsliste.update({ware: menge})
                print("Einkaufsliste wurde erfolgreich aktualisiert.")
            else:
                print("In Ordnung. Die Liste wurde nicht aktualisiert.")
    except:
        print("Die Ware befindet sich noch nicht auf der Liste und wird hinzugefügt.")
        einkaufsliste.update({ware: menge})

    print("Auf der Einkaufsliste befindet sich: ", einkaufsliste)

def loeschen():
    print("Auf der Einkaufsliste befindet sich: ", einkaufsliste)
    ware_vorhanden = False
    while not ware_vorhanden:
        ware = input("Bitte geben Sie ein, was Sie löschen möchten: ")
        try:
            einkaufsliste.pop(ware)
            ware_vorhanden = True
        except:
            print("Die Ware",ware,"befindet sich nicht auf der Einkaufsliste.")
    print("Löschen erfolgreich. Neue Einkaufsliste: ", einkaufsliste)

# Hauptprogramm
print("Willkommen zum Einkaufslisten-Programm")
weitermachen = True
while weitermachen:
    wahl = zahleneingabe("Sie haben folgende Möglichkeiten: \n (1) Liste anzeigen \n (2) Ware hinzufügen \n (3) Ware löschen \n (4) Programm beenden \n")
    if wahl == 1:
        print("Auf der Einkaufsliste befindet sich: \n", einkaufsliste)
    elif wahl == 2:
        hinzufuegen()
    elif wahl == 3:
        loeschen()
    elif wahl == 4:
        weitermachen = False
    else:
        print("Ihre Wahl konnte nicht zugeordnet werden.")