# Programmieren Sie das Spiel Stein-Schere-Papier für zwei Spieler. Jeder Spieler kann entweder
# Stein, Schere oder Papier wählen.
# Die Regeln:
# Stein schlägt Schere Schere schlägt Papier Papier schlägt den Stein
# • Fragen Sie nach dem Namen der Spieler
# • Programmieren Sie eine Funktion, die den Gewinner ermittelt
# • Geben Sie den Gewinner aus.
# Optimieren Sie das Programm, so dass Sie Programmteile in Funktionen auslagern.

#############################
#### Variablendefinition ####
#############################

punkte_spieler_1 = 0
punkte_spieler_2 = 0

#############################
#### Funktionsdefinition ####
#############################

def spielername(nummer):
    """
    The function "spielername" prompts the user to enter their name and returns it, while also greeting
    them with their assigned player number.
    
    :param nummer: The parameter "nummer" is an integer representing the player number
    :return: the name entered by the player.
    """
    print("Hallo Spieler", nummer, ".")
    name = input("Bitte gib deinen Namen ein: ")
    return name

def spielentscheidung(spielername):
    """
    The function prompts a player to make a decision between rock, paper, or scissors and only accepts
    valid inputs.
    
    :param spielername: The parameter `spielername` is a string representing the name of the player who
    is being prompted to make a decision in a game of rock-paper-scissors
    :return: the player's decision (either "stein", "schere", or "papier") after ensuring that the input
    is valid.
    """
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
    """
    The function determines the winner of a rock-paper-scissors game between two players based on their
    choices.
    
    :param entscheidung_1: The decision made by player 1, which can be 'stein' (rock), 'papier' (paper),
    or 'schere' (scissors)
    :param entscheidung_2: The decision made by the second player, which can be either "stein" (rock),
    "papier" (paper), or "schere" (scissors)
    :param spieler_1: The name or identifier of the first player
    :param spieler_2: The variable spieler_2 represents the name or identifier of the second player in a
    game of rock-paper-scissors
    :return: the winner of a rock-paper-scissors game based on the decisions made by two players. If
    there is no winner, it returns "unentschieden" (which means "tie" in German).
    """
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

# This code block is the main loop of the program that runs the game of rock-paper-scissors between
# two players. It repeatedly prompts each player to make a decision, determines the winner based on
# their choices, and assigns points to the winner in a best-of-three format. If one player reaches
# three points, the loop ends and the program asks if the players want to play again. If the game ends
# in a tie, the loop repeats until there is a winner.

while wiederholung:
    entscheidung_1 = spielentscheidung(spieler_1)
    entscheidung_2 = spielentscheidung(spieler_2)
    gewinner = gewinnermittlung(entscheidung_1.lower(), entscheidung_2.lower(), spieler_1, spieler_2)
    if gewinner != "unentschieden":
        print("Super.", gewinner, "hat einen weiteren Punkt bekommen!")
        # Zuweisen von Punkten für BO3 Spielmodus
        if gewinner == spieler_1:
            punkte_spieler_1 += 1
        elif gewinner == spieler_2:
            punkte_spieler_2 += 1   
        if punkte_spieler_1 < 3 and punkte_spieler_2 < 3:
            print("Weiter geht's ... Best of 3.")
            print("Punktestand von", spieler_1, ":", punkte_spieler_1)
            print("Punktestand von", spieler_2, ":", punkte_spieler_2)
        else:
            if punkte_spieler_1 == 3:
                print("Herzlichen Glückwunsch", spieler_1, "du hast gewonnen.")
            elif punkte_spieler_2 == 3:
                print("Herzlichen Glückwunsch", spieler_2, "du hast gewonnen.")               
            entscheidung = input("Wollt ihr noch Mal spielen (ja/nein): ")
            if entscheidung.lower() == "nein":
                wiederholung = False
            else:
                print("Alles klar, neue Runde...")
    else:
        print("Unentschieden! Wiederholungsrunde...")