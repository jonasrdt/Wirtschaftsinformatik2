# Aufgabe 1 - Übung 6
# 
# Teil a)
# Wirtschaftsinformatik II
# Labor - Übung 6
# Programmieren Sie das Spiel Stein-Schere-Papier für zwei Spieler. Jeder Spieler kann entweder Stein, Schere oder Papier wählen.
# Die Regeln:
# Stein schlägt Schere Schere schlägt Papier Papier schlägt den Stein
# • Fragen Sie nach dem Namen der Spieler
# • Programmieren Sie eine Funktion, die den Gewinner ermittelt
# • Geben Sie den Gewinner aus.
# Optimieren Sie das Programm, so dass Sie Programmteile in Funktionen auslagern.
# Teil b)
# Erweitern Sie das Spiel so, dass man es auch alleine spielen kann, also mit einem Computergegner.

def trenner(anzahl):
    for i in range(anzahl):
        print("-", end="")
    print()

def eingabeSpielername(spielernummer):
    gueltige_eingabe = False
    while not gueltige_eingabe:
        trenner(50)
        print("Bitte geben Sie den Namen für Spieler", spielernummer, "ein", end="")
        spielername = input(": ")
        if spielername == "":
            print("Bitte geben Sie einen vollständigen Namen ein.")
        else:
            gueltige_eingabe = True
    print("Spieler", spielernummer, "ist mit dem Namen", spielername, "eingetragen.")
    trenner(50)
    return spielername

def begruessungSpieler():
    trenner(50)
    print("Willkommen bei Stein-Schere-Papier.")
    trenner(50)
    print("Bitte geben Sie die Namen der Spieler ein.")

def spielmechanik():
    trenner(50)
    gueltige_eingabe = False
    while not gueltige_eingabe:
        eingabe = input("Wählen Sie zwischen Stein, Schere oder Papier: ")
        if eingabe.upper() == "":
            print("Das war keine gültige Eingabe.")
        else:
            gueltige_eingabe = True
    return eingabe

def vergleichsmechanik(spieler1, eingabe1, spieler2, eingabe2):
    if eingabe1 == eingabe2:
        ergebnis = "Unentschieden!"
    if eingabe1 == "STEIN" and eingabe2 == "SCHERE":
        print(spieler2, "hat gewonnen.")
    elif eingabe1 == "STEIN" and eingabe2 == "PAPIER":
        print(spieler1, "hat gewonnen")
    elif eingabe1 == "PAPIER" and eingabe2 == "":
        print("")

begruessungSpieler()
spieler1 = eingabeSpielername(1)
spieler2 = eingabeSpielername(2)
eingabe_spieler1 = spielmechanik()
eingabe_spieler2 = spielmechanik()
vergleichsmechanik(spieler1, eingabe_spieler1, spieler2, eingabe_spieler2)