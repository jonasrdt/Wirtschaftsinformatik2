import random

def spiel_gegen_computer():
    entscheidung_computer = random.choice(["stein", "papier", "schere"])
    print("Der Computer hat:", entscheidung_computer, "gewählt.")
    return entscheidung_computer
    
def spielername(nummer):
    print("Willkommen Spieler", nummer)
    name = input("Bitte gib deinen Namen ein: ")
    return name

def spielentscheidung(spielernamen):
    print("Los geht's", spielernamen, "!")
    entscheidung = input("Bitte triff deine Entscheidung (Stein/Schere/Papier): ").lower()
    return entscheidung

def gewinnermittlung(entscheidung_1, entscheidung_2, spieler_1, spieler_2):
    if entscheidung_1 == "stein" and entscheidung_2 == "papier":
        print(spieler_2, "hat gewonnen.")
    elif entscheidung_1 == "papier" and entscheidung_2 == "stein":
        print(spieler_1, "hat gewonnen.")
    elif entscheidung_1 == "schere" and entscheidung_2 == "papier":
        print(spieler_1, "hat gewonnen.")
    elif entscheidung_1 == "papier" and entscheidung_2 == "schere":
        print(spieler_2, "hat gewonnen.")
    elif entscheidung_1 == "stein" and entscheidung_2 == "schere":
        print(spieler_1, "hat gewonnen.")
    elif entscheidung_1 == "schere" and entscheidung_2 == "stein":
        print(spieler_2, "hat gewonnen.")
    else:
        print("Unentschieden. :-)")

#### Hauptprogramm ####
spieler_1 = spielername(1)
spieler_2 = spielername(2)

entscheidung_1 = spielentscheidung(spieler_1)
entscheidung_2 = spielentscheidung(spieler_2)
gewinnermittlung(entscheidung_1, entscheidung_2, spieler_1, spieler_2)