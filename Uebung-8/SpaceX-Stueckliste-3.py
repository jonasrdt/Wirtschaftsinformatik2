stueckliste = []

def bauteilHinzufuegen(bauteil, menge):
    stueckliste.append([bauteil, menge])
    print("Auf der Stückliste befindet sich:", stueckliste)

def zahlenEingabe():
    richtige_eingabe = False
    while not richtige_eingabe:
        try:
            menge = float(input("Bitte geben Sie eine Menge ein: "))
            richtige_eingabe = True
            return menge
        except:
            print("Bitte geben Sie nur Zahlen an.")

def weitereEingabe():
    entscheidung = input("Wollen Sie noch etwas eingeben (ja/nein): ")
    if entscheidung.lower() == "nein":
        return False
    else:
        return True

mehr_eingabe = True
while mehr_eingabe:
    bauteil = input("Bitte geben Sie ein Bauteil ein: ")
    menge = zahlenEingabe()
    print("Es werden", menge, bauteil, "hinzugefügt.")
    bauteilHinzufuegen(bauteil, menge)
    mehr_eingabe = weitereEingabe()

