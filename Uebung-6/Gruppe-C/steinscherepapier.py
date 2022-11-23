# Programmieren Sie das Spiel Stein-Schere-Papier für zwei Spieler. Jeder Spieler kann entweder Stein, Schere oder Papier wählen.
# Die Regeln:
# Stein schlägt Schere Schere schlägt Papier Papier schlägt den Stein
# • Fragen Sie nach dem Namen der Spieler
# • Programmieren Sie eine Funktion, die den Gewinner ermittelt
# • Geben Sie den Gewinner aus.
# Optimieren Sie das Programm, so dass Sie Programmteile in Funktionen auslagern.

#################################        
###### Funktionsdefinition ######
#################################

def spielername(spielernummer):
    print("Hallo Spieler", spielernummer, "bitte gib deine Namen ein.")
    spielername = input("Dein Name:")
    return spielername

def spielentscheidung():
    print("Bitte wähle zwischen Schere, Stein oder Papier.")
    spielentscheidung = input("Deine Spielentscheidung: ")
    korrekte_spielentscheidung = False
    while not korrekte_spielentscheidung:
        if spielentscheidung.lower() == "schere" or spielentscheidung.lower() == "stein" or spielentscheidung.lower() == "papier":
            print("Du hast dich für", spielentscheidung, "entschieden. Bestimmt eine gute Wahl.")
            korrekte_spielentscheidung = True
        else:
            print("Bitte gib nur Schere, Stein oder Papier ein.")
    return spielentscheidung

def gewinner(spielentscheidung_1, spielentscheidung_2, spieler_1, spieler_2):
    if spielentscheidung_1 == spielentscheidung_2:
        print("Unentschieden!", spieler_1, "und", spieler_2, "haben sich gleich entschieden.")
    elif spielentscheidung_1.lower() == "schere" and spielentscheidung_2.lower() == "stein":
        print(spieler_2, "hat gewonnen.", spielentscheidung_2, "schlägt", spielentscheidung_1,".")
    elif spielentscheidung_1.lower() == "stein" and spielentscheidung_2.lower() == "schere": 
        print(spieler_1, "hat gewonnen.", spielentscheidung_1, "schlägt", spielentscheidung_2,".")
    elif spielentscheidung_1.lower() == "papier" and spielentscheidung_2.lower() == "stein":
        print(spieler_1, "hat gewonnen.", spielentscheidung_1, "schlägt", spielentscheidung_2,".")
    elif spielentscheidung_1.lower() == "stein" and spielentscheidung_2.lower() == "papier":
        print(spieler_2, "hat gewonnen.", spielentscheidung_2, "schlägt", spielentscheidung_1,".")
    elif spielentscheidung_1.lower() == "schere" and spielentscheidung_2.lower() == "papier":
        print(spieler_1, "hat gewonnen.", spielentscheidung_1, "schlägt", spielentscheidung_2,".")
    elif spielentscheidung_1.lower() == "papier" and spielentscheidung_2.lower() == "schere":
        print(spieler_2, "hat gewonnen.", spielentscheidung_2, "schlägt", spielentscheidung_1,".")

###########################        
###### Hauptprogramm ######
###########################
