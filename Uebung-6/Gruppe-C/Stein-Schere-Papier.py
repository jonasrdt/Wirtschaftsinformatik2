

# # Möglichkeit 1
spieler_1 = input("Bitte geben Sie den Namen von Spieler 1 ein: ")
spieler_2 = input("Bitte geben Sie den Namen von Spieler 2 ein: ")

entscheidung_1  = input("Bitte geben Sie Stein, Schere oder Papier ein: ")

# Möglichkeit 2
def spielername(nummer):
    print("Bitte geben Sie den Namen für Spieler", nummer, "ein.")
    name = input("Name: ")
    name = name.capitalize()
    return name

def spielentscheidung():
    print("Bitte geben Sie Stein, Schere oder Papier ein: ")
    richtige_eingabe = False
    while not richtige_eingabe:
        entscheidung = input("Entscheidung: ")
        if entscheidung.lower() != "stein" or entscheidung.lower() != "schere" or entscheidung.lower() != "papier":
            print("Bitte geben Sie nur Stein, Schere oder Papier ein.")
        else:
            richtige_eingabe = True
    entscheidung.lower()
    return entscheidung

spieler_1 = spielername(1)
spieler_2 = spielername(2)
entscheidung_1 = spielentscheidung()
