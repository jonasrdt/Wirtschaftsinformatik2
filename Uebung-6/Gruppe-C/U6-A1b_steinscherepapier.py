# Programmieren Sie das Spiel Stein-Schere-Papier für zwei Spieler. Jeder Spieler kann entweder Stein, Schere oder Papier wählen.
# Die Regeln:
# Stein schlägt Schere Schere schlägt Papier Papier schlägt den Stein
# • Fragen Sie nach dem Namen der Spieler
# • Programmieren Sie eine Funktion, die den Gewinner ermittelt
# • Geben Sie den Gewinner aus.
# Optimieren Sie das Programm, so dass Sie Programmteile in Funktionen auslagern.

import random
random.seed()

#################################        
###### Funktionsdefinition ######
#################################

def spielername(spielernummer):
    print("Hallo Spieler", spielernummer, "bitte gib deine Namen ein.")
    spielername = input("Dein Name: ")
    return spielername

def spielentscheidung(spielername):
    print(spielername, "bitte wähle zwischen Schere, Stein oder Papier.")
    korrekte_spielentscheidung = False
    while not korrekte_spielentscheidung:
        spielentscheidung = input("Deine Spielentscheidung: ")
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
        
def computerwahl():
    entscheidung = random.randint(1,3)
    if entscheidung == 1:
        return "Schere"
    elif entscheidung == 2:
        return "Papier"
    elif entscheidung == 3:
        return "Stein"   
        
def trenner(anzahl):
    for i in range(anzahl):
        print("*", end= " ")
    print()

###########################        
###### Hauptprogramm ######
###########################
trenner(50)
print("Willkommen zu Stein, Schere, Papier.")
trenner(50)
korrekte_eingabe = False
while not korrekte_eingabe:
    try:
        spielerzahl = int(input("Wie viele Spieler seid ihr (1 oder 2): "))
        if spielerzahl == 2:
            spieler_1 = spielername(1)
            spieler_2 = spielername(2)
            trenner(50)
            spielentscheidung_1 = spielentscheidung(spieler_1)
            trenner(50)
            spielentscheidung_2 = spielentscheidung(spieler_2)
            trenner(50)
            gewinner(spielentscheidung_1, spielentscheidung_2, spieler_1, spieler_2)
            trenner(50)
        elif spielerzahl == 1:
            spieler_1 = spielername(1)
            spielentscheidung_1 = spielentscheidung(spieler_1)
            computerentscheidung = computerwahl()
            gewinner(spielentscheidung_1, computerentscheidung, spieler_1, "der Computer")
        else:
            print("Bitte gib nur eine 1 oder 2 ein.")
            korrekte_eingabe = True
    except:
        print("Bitte geben Sie nur Zahlen ein.")