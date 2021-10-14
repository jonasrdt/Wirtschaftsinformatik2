# Zufallsgenerator Spiel
# Modulimport
import random

def berechnung(zahl1, zahl2, operator):
    if operator == "+":
        ergebnis = zahl1 + zahl2
    elif operator == "-":
        ergebnis = zahl1 - zahl2
    elif operator == "*":
        ergebnis = zahl1 * zahl2
    elif operator == "/":
        ergebnis = zahl1 / zahl2
    else:
        print("Der von Ihnen eingegebene Operator", operator, "ist nicht gültig.")
    print(zahl1, operator, zahl2)
    return ergebnis

weiterspielen = True

while weiterspielen:
    # Belegen der Variablen mit randomisierten Zahlen
    erste_zahl = random.randint(1,10)
    zweite_zahl = random.randint(1,10)

    wrong_operator = True
    while wrong_operator:    
        operator = input("Was wollen Sie rechnen *, -, +, / : ")
        if operator == "*" or operator == "-" or operator == "/" or operator == "+":
            wrong_operator = False
        else:
            print("Das war leider kein gültiger Operator. Bitte geben Sie nur + - * / ein.")

    ergebnis = berechnung(erste_zahl, zweite_zahl, operator)

    for zaehler in range(3):  
        # Nutzer zur Eingabe einer Lösung auffordern
        nutzer_loesung = int(input("Bitte geben Sie die Lösung ein: "))
        if nutzer_loesung == ergebnis:
            print("Glückwunsch", nutzer_loesung, "ist richtig.")
            break
        else:
            print("Schade, das war leider nicht korrekt.")
            if zaehler == 2:
                print("Die richtige Lösung wäre gewesen:", ergebnis)
            
    
    # Fragen, ob der Nutzer weiterspielen will
    nutzer_nachfrage = input("Wollen Sie weiterspielen (ja/nein): ")
    # Wenn nicht, dann wird "weiterspielen" auf False gesetzt
    if nutzer_nachfrage.lower() == "nein":
        weiterspielen = False
    # Andernfalls, geht es weiter!
    else:
        print("Weiter geht die wilde Fahrt.")

