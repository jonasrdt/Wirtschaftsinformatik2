
# Initialisieren der Variable
stueckliste = []

weiterer_artikel = True
while weiterer_artikel:
    artikel = input("Bitte geben Sie den Namen des Artikels ein, den Sie der Stückliste hinzufügen wollen: ")
    stueckliste.append(artikel)
    entscheidung = input("Wollen Sie noch etwas hinzufügen (ja/nein): ")
    if entscheidung.lower() == "nein":
        weiterer_artikel = False

print("Auf der Stückliste befinden sich die folgenden Artikel:")
for element in stueckliste:
    print("- ", element)
