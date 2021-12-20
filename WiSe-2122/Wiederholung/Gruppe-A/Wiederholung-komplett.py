# Entwickeln Sie ein Programm, welches eine Einkaufsliste erstellt.
# Der Nutzer soll die Möglichkeit haben, Waren und deren Menge zu der Einkaufsliste hinzuzufügen.
# Ist die Ware bereits auf der Einkaufsliste vorhanden, so soll dies zuerst ausgegeben und gefragt werden,
# ob die Menge geändert werden soll.

# Variablendefinition
einkaufsliste = {}

# Funktionsdefinition
def trenner(anzahl):
    for i in range(anzahl):
        print("-", end="")
    print()

def zahleneingabe(text):
    falsche_eingabe = True
    while falsche_eingabe:
        try:
            zahl = int(input(text))
            falsche_eingabe = False
        except:
            print("Bitte geben Sie nur ganze Zahlen ein.")
    return zahl

def artikelHinzufuegen():
    # Hinzufügen eines Artikels zur Einkaufsliste
    # Abfragen des Artikelnamens
    artikel = input("Bitte geben Sie einen Artikel ein: ")
    # Abfragen der Artikelmenge
    menge = zahleneingabe("Bitte geben Sie die Menge an: ")
    # Prüfen, ob der Artikel bereits in der Einkaufsliste vorhanden ist
    if artikel in einkaufsliste:
        print("Der Artikel", artikel, "befindet sich bereits mit", einkaufsliste[artikel], "Stück auf der Liste.")
        entscheidung = input("Wollen Sie den Artikel ersetzen (ja/nein): ")
        # Eintrag aktualisieren, wenn entscheidung == "ja"
        if entscheidung.lower() == "ja":
            einkaufsliste.update({artikel: menge})
    # Befindet sich der Artikel noch nicht auf der Liste, wird er hinzugefügt
    else:
        print(artikel,"befindet sich noch nicht auf der Liste und wird hinzugefügt.")
        einkaufsliste.update({artikel: menge})
    # Ausgabe dessen, was bereits auf der Liste steht
    print("Auf der Einkaufsliste befindet sich: ", einkaufsliste)

def artikelLoeschen():
    print("Auf der Liste befindet sich:", einkaufsliste)
    loeschen = input("Welchen Artikel wollen Sie löschen: ")
    if loeschen in einkaufsliste:
        einkaufsliste.pop(loeschen)
        print("Der Artikel", loeschen,"wurde erfolgreich gelöscht.")
    else:
        print("Der Artikel",loeschen,"befindet sich nicht auf der Einkaufsliste.")
        
# Hauptprogramm
trenner(50)
print("Willkommen beim Einkaufslisten-Programm")
print("Im Folgenden können Sie Artikel zu Ihrer Einkaufsliste hinzufügen, löschen, ändern und anzeigen.")
trenner(50)
weiter_hinzufuegen = True
while weiter_hinzufuegen:
    trenner(50)
    entscheidung = int(input("Wollen Sie: \n(1) einen Artikel hinzufügen \n(2) einen Artikel löschen \n(3) die Einkaufsliste anzeigen \n(4) das Programm beenden \n Eingabe: "))
    trenner(50)
    if entscheidung == 1:
        artikelHinzufuegen()
    elif entscheidung == 2:
        artikelLoeschen()
    elif entscheidung == 3:
        print("Auf der Einkaufsliste steht:", einkaufsliste)
    elif entscheidung == 4:
        print("Bitte.Danke.Tschüß.")
        weiter_hinzufuegen = False
    else:
        print("Ihre Eingabe konnte nicht zugeordnet werden.")
