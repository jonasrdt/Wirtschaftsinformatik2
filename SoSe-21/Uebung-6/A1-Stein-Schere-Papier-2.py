# Programmieren Sie das Spiel Stein-Schere-Papier für zwei Spieler. Jeder Spieler kann entweder Stein, Schere oder Papier wählen.
# Die Regeln:
# Stein schlägt Schere Schere schlägt Papier Papier schlägt den Stein
# • Fragen Sie nach dem Namen der Spieler
# • Programmieren Sie eine Funktion, die den Gewinner ermittelt
# • Geben Sie den Gewinner aus.
# Optimieren Sie das Programm, so dass Sie Programmteile in Funktionen auslagern.
 
import random


# Definieren von Funktion für die Eingabe des Spielernamens
def spielerNamenErfassen(spielernummer):
    print("Spieler", spielernummer, "bitte geben Sie Ihren Namen ein: ")
    spielername = input()
    return spielername

def spielerEingabeErfassen(spielername):
    print(spielername, "Bitte geben Sie Stein, Schere oder Papier ein:")
    entscheidung = input()
    return entscheidung

def gewinnerErmitteln(entscheidung_1, spieler_1, entscheidung_2, spieler_2):
    if (entscheidung_1.upper() == entscheidung_spieler_2.upper()):
        print("Unentschieden!")
        return False
 
    elif (entscheidung_1.upper() == "STEIN" and entscheidung_2.upper() == "PAPIER"):
        print(spieler_2, "hat", entscheidung_2, "gewählt und gewinnt.")
        return True
 
    elif (entscheidung_1.upper() == "STEIN" and entscheidung_2.upper() == "SCHERE"):
        print(spieler_1, "hat", entscheidung_1, "gewählt und gewinnt.")
        return True
 
    elif (entscheidung_1.upper() == "SCHERE" and entscheidung_2.upper() == "STEIN"):
        print(spieler_2, "hat", entscheidung_2, "gewählt und gewinnt.")
        return True
 
    elif (entscheidung_1.upper() == "SCHERE" and entscheidung_2.upper() == "PAPIER"):
        print(spieler_1, "hat", entscheidung_1, "gewählt und gewinnt.")
        return True
 
    elif (entscheidung_1.upper() == "PAPIER" and entscheidung_2.upper() == "SCHERE"):
        print(spieler_2, "hat", entscheidung_2, "gewählt und gewinnt.")
        return True
 
    elif (entscheidung_1.upper() == "PAPIER" and entscheidung_2.upper() == "STEIN"):
        print(spieler_1, "hat", entscheidung_1, "gewählt und gewinnt.")
        return True

def computerEntscheidung():
    zufallszahl = random.randint(1,3)
    if zufallszahl == 1:
        return "Stein"
    elif zufallszahl == 2:
        return "Papier"
    else:
        return "Schere"

###### Hauptprogramm ######

alleineoderzuzweit = input("Möchtest du gegen den Computer oder gegen eine zweite Person spielen (Computer/Person)?")
if alleineoderzuzweit.upper() == "PERSON":
    # Starten des Programms
    spieler_1 = spielerNamenErfassen(1)
    spieler_2 = spielerNamenErfassen(2)
    gewinner = False
    while not gewinner:
        entscheidung_spieler_1 = spielerEingabeErfassen(spieler_1)
        entscheidung_spieler_2 = spielerEingabeErfassen(spieler_2)
        gewinner = gewinnerErmitteln(entscheidung_spieler_1, spieler_1, entscheidung_spieler_2, spieler_2)
elif alleineoderzuzweit.upper() == "COMPUTER":
    print("Okay, dann spielst du gegen den Computer.")
    spieler_1 = spielerNamenErfassen(1)
    spieler_2 = "Computer"
    gewinner = False
    while not gewinner:
        entscheidung_spieler_1 = spielerEingabeErfassen(spieler_1)
        entscheidung_spieler_2 = computerEntscheidung()
        gewinner = gewinnerErmitteln(entscheidung_spieler_1, spieler_1, entscheidung_spieler_2, spieler_2)
else:
    print("Deine Eingabe konnte leider nicht verarbeitet werden.")

