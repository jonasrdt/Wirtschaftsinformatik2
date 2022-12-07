# Es soll ein Spiel entwickelt werden, welches zufällig Zahlen vorschlägt
# und den Nutzer eine Antwort berechnen lässt. Der Nutzer hat drei Chancen
# die richtige Antworte einzugeben. Sollte er die richtige Antwort nicht ermitteln
# verliert er.

import random
random.seed()
anzahl_versuche = 3

def trenner(anzahl):
    """
    It prints a line of asterisks
    
    :param anzahl: The number of asterisks to print
    """
    for i in range(anzahl):
        print("*", end= " ")
    print()
    
def loesungsermittlung(anzahl_versuche, loesung):
    """
    The function takes two arguments, the number of attempts and the solution, and asks the user to
    enter the solution. 
    If the user enters the correct solution, the function prints a congratulatory message and stops. 
    If the user enters the wrong solution, the function prints a message that the solution was wrong and
    how many attempts the user has left. 
    If the user has no attempts left, the function prints a message that the game is over
    
    :param anzahl_versuche: The number of attempts the user has to guess the correct answer
    :param loesung: The solution to the problem
    """
    for versuch in range(1,anzahl_versuche+1):
        nutzereingabe = round(float(input("Bitte geben Sie die Lösung, gerundet auf zwei Nachkommastellen ein: ")),2)
        trenner(15)
        if nutzereingabe == round(loesung,2):
            print("Juhu. Sie haben das richtige Ergebnis berechnet.")
            trenner(15)
            break
        else:
            print("Das war leider nicht richtig.")
            print("Das war Ihr", versuch,"Versuch. Sie haben noch", anzahl_versuche - versuch,"Versuche übrig.")
            trenner(15)
            if versuch == 3:
                print("Schade, das war wohl nix. Spiel vorbei")

def rechenverfahren():
    """
    The function rechenverfahren() asks the user to input a mathematical operation and returns the
    operation if it is valid
    :return: the input of the user.
    """
    rechenoperationen = ["+", "-", "/", "*"]
    korrektes_rechenverfahren = False
    while not korrektes_rechenverfahren:
        rechenverfahren = input("Bitte geben Sie die Rechenoperation ein, die Sie durchführen wollen (+,-,/,*): ")
        if rechenverfahren in rechenoperationen:
            return rechenverfahren
        else:
            print("Bitte geben Sie nur +, -, /, * ein: ")
  

def rechenaufgabe(operator, erste_zahl, zweite_zahl):
    """
    The function `rechenaufgabe` takes three arguments: `operator`, `erste_zahl`, and `zweite_zahl`. It
    prints a string that contains the first two arguments and the third argument. It then creates a
    string that contains the first two arguments and the third argument, and evaluates that string. It
    returns the result of the evaluation
    
    :param operator: The operator to use in the calculation
    :param erste_zahl: The first number in the equation
    :param zweite_zahl: The second number in the equation
    :return: The solution of the math problem.
    """
    print("Die Aufgabe lautet:", erste_zahl, operator, zweite_zahl)
    aufgabe = str(erste_zahl) + operator + str(zweite_zahl)
    loesung = eval(aufgabe)
    return loesung

############################
####### Hauptprogramm ######
############################

spielentscheidung = True
while spielentscheidung:
    erste_zahl = random.randint(1,15)
    zweite_zahl = random.randint(1,15)
    loesungsermittlung(anzahl_versuche, rechenaufgabe(rechenverfahren(), erste_zahl, zweite_zahl))
    weiterspielen = input("Wollen Sie weiterspielen (ja/nein): ")
    if weiterspielen.lower() == "nein":
        spielentscheidung = False
        print("Alles klar. Viel Spaß noch. :-)")

