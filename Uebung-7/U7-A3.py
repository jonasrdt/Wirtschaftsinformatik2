#### Variablendefinition ####
# Definieren der Variable 'stueckliste'
stueckliste = []

#### Funktionsdefinition ####
def zahleneingabe(art, bauteil):
    korrekte_eingabe = False
    while not korrekte_eingabe:
        try:
            print("Eingabe der", art, "für", bauteil, ".")
            zahl = int(input("Bitte geben Sie den passenden Wert an: "))
            korrekte_eingabe = True
        except:
            print("Bitte nur Zahlen eingeben.")
    return zahl

#### Hauptprogramm ####
# while-Schleife die so lange läuft, wie der Nutzer Teile zu der Stückliste hinzufügen möchte
erneute_eingabe = True
while erneute_eingabe:
    bauteil = input("Bitte geben Sie ein, was Sie zu der Stückliste hinzufügen wollen: ")
    menge = zahleneingabe("Menge", bauteil)
    artikelnummer = zahleneingabe("Artikelnummer", bauteil)
    stueckliste.append([artikelnummer, bauteil, menge])
    # Abprüfen, ob der User noch mehr Eingaben tätigen möchte
    entscheidung = input("Wollen Sie noch ein Bauteil hinzufügen (ja/nein): ")
    if entscheidung.lower() == "nein":
        erneute_eingabe = False

print("Auf der Stückliste steht:", stueckliste)
