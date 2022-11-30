
# Initialisieren der Variable
stueckliste = []

weiterer_artikel = True
while weiterer_artikel:
    artikel = input("Bitte geben Sie den Namen des Artikels ein, den Sie der Stückliste hinzufügen wollen: ")
    korrekte_eingabe = False
    while not korrekte_eingabe:
        try:
            menge = int(input("Bitte geben Sie Menge des Artikels an: "))
            korrekte_eingabe = True
        except:
            print("Bitte geben Sie nur Zahlen ein.")
    stueckliste.append([artikel, menge])
    entscheidung = input("Wollen Sie noch etwas hinzufügen (ja/nein): ")
    if entscheidung.lower() == "nein":
        weiterer_artikel = False

print("Auf der Stückliste befinden sich die folgenden Artikel:")
for element in stueckliste:
    print(element[0], "befindet sich", element[1], "Mal auf der Liste.")
