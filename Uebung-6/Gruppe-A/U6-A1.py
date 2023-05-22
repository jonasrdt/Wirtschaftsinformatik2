# Programmieren Sie das Spiel Stein-Schere-Papier für zwei Spieler. Jeder Spieler kann entweder
# Stein, Schere oder Papier wählen.
# Die Regeln:
# Stein schlägt Schere Schere schlägt Papier Papier schlägt den Stein
# • Fragen Sie nach dem Namen der Spieler
# • Programmieren Sie eine Funktion, die den Gewinner ermittelt
# • Geben Sie den Gewinner aus.
# Optimieren Sie das Programm, so dass Sie Programmteile in Funktionen auslagern.




#############################
#### Funktionsdefinition ####
#############################

def spielername(nummer):
    print("Hallo Spieler", nummer, ".")
    name = input("Bitte gib deinen Namen ein: ")
    return name

def spielentscheidung(spielername):
    print(spielername, "bitte triff deine Entscheidung.")
    richtige_entscheidungen = ['stein', 'schere', 'papier']
    korrekte_eingabe = False
    while not korrekte_eingabe:
        entscheidung = input("Stein/Schere/Papier: ")
        if entscheidung.lower() in richtige_entscheidungen:
            korrekte_eingabe = True
            return entscheidung
        else:
            print("Bitte gib nur Stein/Schere/Papier ein.")

def gewinnermittlung(entscheidung_1, entscheidung_2, spieler_1, spieler_2):
    if entscheidung_1 == 'stein' and entscheidung_2 == 'papier':
        return spieler_2
    elif entscheidung_1 == 'papier' and entscheidung_2 == 'stein':
        return spieler_1
    elif entscheidung_1 == 'stein' and entscheidung_2 == 'schere':
        return spieler_1
    elif entscheidung_1 == 'schere' and entscheidung_2 == 'stein':
        return spieler_2
    elif entscheidung_1 == 'schere' and entscheidung_2 == 'papier':
        return spieler_1
    elif entscheidung_1 == 'papier' and entscheidung_2 == 'schere':
        return spieler_2
    else:
        return "unentschieden"
    

#############################
####### Hauptprogramm #######
#############################

spieler_1 = spielername(1)
spieler_2 = spielername(2)
wiederholung = True
while wiederholung:
    entscheidung_1 = spielentscheidung(spieler_1)
    entscheidung_2 = spielentscheidung(spieler_2)
    gewinner = gewinnermittlung(entscheidung_1.lower(), entscheidung_2.lower(), spieler_1, spieler_2)
    if gewinner != "unentschieden":
        print("Super.", gewinner, "hat gewonnen!")
        entscheidung = input("Wollt ihr noch Mal spielen (ja/nein): ")
        if entscheidung.lower() == "nein":
            wiederholung = False
        else:
            print("Alles klar, neue Runde...")
    else:
        print("Unentschieden! Wiederholungsrunde...")