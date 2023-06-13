# Programmieren Sie das Spiel Stein-Schere-Papier für zwei Spieler. Jeder Spieler kann
# entweder Stein, Schere oder Papier wählen.
# Die Regeln:
# Stein schlägt Schere; Schere schlägt Papier; Papier schlägt den Stein
# • Fragen Sie nach dem Namen der Spieler
# • Programmieren Sie eine Funktion, die den Gewinner ermittelt
# • Geben Sie den Gewinner aus.
# Optimieren Sie das Programm, so dass Sie Programmteile in Funktionen auslagern.

### Funktionsdefinition ###
def spielerinnummer(nummer):
    """
    This function welcomes a player and asks for their player number.
    
    :param nummer: The parameter "nummer" is a variable that represents the player's number. It is used
    to welcome the player and identify them by their number
    :return: the input value of the variable "spielerinnummer", which is the player's name or
    identifier.
    """
    print("Willkommen Spielerin Nummer", nummer)
    spielerinnummer = input("Bitte gib deinen Spielerin ein: ")
    return spielerinnummer

def entscheidung(spielerin):
    """
    The function allows a player to input their choice of "rock", "scissors", or "paper" and returns
    their choice.
    
    :param spielerin: The parameter "spielerin" is a string representing the name of the player who will
    be making a decision in the game
    :return: the player's valid choice of "stein", "schere", or "papier".
    """
    print("Hallo", spielerin, "jetzt wird's knifflig!")
    moegliche_entscheidungen = ["stein", "schere", "papier"]
    richtige_entscheidung = False
    while not richtige_entscheidung:
        entscheidung = input("Bitte geben Sie Stein, Schere oder Papier ein: ")
        if entscheidung.lower() in moegliche_entscheidungen:
            print("Du hast", entscheidung, "eingeben. Einverstanden.")
            richtige_entscheidung = True
        elif entscheidung.lower() == "brunnen":
            print("Ohne Brunnen, du Assi. Bitte gib nur Stein, Schere oder Papier ein.")
        else:
            print("Bitte gib nur Stein, Schere oder Papier ein.")
    return entscheidung    

def winner(entscheidung_1, entscheidung_2, spielerin_1, spieler_2):
    """
    The function determines the winner of a game of rock-paper-scissors between two players based on
    their choices.
    
    :param entscheidung_1: The decision made by the first player (either "stein", "papier", or "schere")
    :param entscheidung_2: `entscheidung_2` is a variable representing the decision made by the second
    player in a game. It could be "stein" (rock), "papier" (paper), or "schere" (scissors)
    :param spielerin_1: The name of the first player (a string)
    :param spieler_2: The name or identifier of the second player in the game
    :return: the name of the winning player or "Unentschieden" (German for "tie") if the game is a tie.
    """
    if entscheidung_1.lower() == "stein" and entscheidung_2.lower() == "papier":
        print("Papier schlägt Stein. Entscheidung 2 gewinnt.")
        return spieler_2
    elif entscheidung_1.lower() == "stein" and entscheidung_2.lower() == "schere":
        print("Stein schlägt Schere. Entscheidung 1 gewinnt.")
        return spieler_1
    elif entscheidung_1.lower() == "papier" and entscheidung_2.lower() == "schere":
        print("Schere schlägt Papier. Entscheidung 2 gewinnt.")
        return spieler_2
    elif entscheidung_2.lower() == "stein" and entscheidung_1.lower() == "papier":
        print("Papier schlägt Stein. Entscheidung 1 gewinnt.")
        return spieler_1
    elif entscheidung_2.lower() == "stein" and entscheidung_1.lower() == "schere":
        print("Stein schlägt Schere. Entscheidung 2 gewinnt.")
        return spieler_2
    elif entscheidung_2.lower() == "papier" and entscheidung_1.lower() == "schere":
        print("Schere schlägt Papier. Entscheidung 1 gewinnt.")
        return spieler_1
    elif entscheidung_1.lower() == entscheidung_2.lower():
        print("Unentschieden!")
        return "Unentschieden"


### Hauptprogramm ###
spielerin_1 = spielerinnummer(1)
spielerin_2 = spielerinnummer(2)
gewinner = False
while not gewinner:
    entscheidung_1 = entscheidung(spielerin_1)
    entscheidung_2 = entscheidung(spielerin_2)
    winner = winner(entscheidung_1, entscheidung_2, spielerin_1, spielerin_2)
    if winner == "Unentschieden":
        print("Unentschieden! Noch Mal ...")
        print("------------------------------")
    else:
        print("Juhu", winner, "hat gewonnen.")