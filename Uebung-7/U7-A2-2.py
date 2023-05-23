stueckliste = []
erneute_eingabe = True
while erneute_eingabe:
    element = input("Bitte geben Sie ein, was Sie zu der Stückliste hinzufügen wollen: ")
    stueckliste.append(element)
    entscheidung = input("Wollen Sie noch ein Element hinzufügen (ja/nein): ")
    if entscheidung.lower() == "nein":
        erneute_eingabe = False