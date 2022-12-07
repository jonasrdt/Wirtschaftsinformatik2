# Es soll ein Spiel entwickelt werden, welches zufällig Zahlen vorschlägt
# und den Nutzer eine Antwort berechnen lässt. Der Nutzer hat drei Chancen
# die richtige Antworte einzugeben. Sollte er die richtige Antwort nicht ermitteln
# verliert er.

import random
random.seed()
anzahl_versuche = 3

def trenner(anzahl):
    for i in range(anzahl):
        print("*", end= " ")
    print()
    

spielentscheidung = True
while spielentscheidung:
    erste_zahl = random.randint(1,15)
    zweite_zahl = random.randint(1,15)
    
    korrektes_verfahren = False
    while not korrektes_verfahren:
        rechenverfahren = input("Bitte geben Sie die Rechenoperation ein, die Sie durchführen wollen (+,-,/,*): ")
        if rechenverfahren == "+":
                print("Die Aufgabe lautet:", erste_zahl, "+", zweite_zahl)
                loesung = erste_zahl + zweite_zahl
                korrektes_verfahren = True
        elif rechenverfahren == "-":
                print("Die Aufgabe lautet:", erste_zahl, "-", zweite_zahl)
                loesung = erste_zahl - zweite_zahl       
                korrektes_verfahren = True 
        elif rechenverfahren == "/":
                print("Die Aufgabe lautet:", erste_zahl, "/", zweite_zahl)
                loesung = erste_zahl / zweite_zahl
                korrektes_verfahren = True     
        elif rechenverfahren == "*":
                print("Die Aufgabe lautet:", erste_zahl, "*", zweite_zahl)
                loesung = erste_zahl * zweite_zahl
                korrektes_verfahren = True
        else:
            print("Bitte geben Sie nur +, -, / oder * ein.")       
             
    trenner(15)
    for versuch in range(1,anzahl_versuche+1):
        nutzereingabe = int(input("Bitte geben Sie die Lösung ein: "))
        trenner(15)
        if nutzereingabe == loesung:
            print("Juhu. Sie haben das richtige Ergebnis berechnet.")
            trenner(15)
            break
        else:
            print("Das war leider nicht richtig.")
            print("Das war Ihr", versuch,"Versuch. Sie haben noch", anzahl_versuche - versuch,"Versuche übrig.")
            trenner(15)
            if versuch == 3:
                print("Schade, das war wohl nix. Spiel vorbei")
    weiterspielen = input("Wollen Sie weiterspielen (ja/nein): ")
    if weiterspielen.lower() == "nein":
        spielentscheidung = False
        print("Alles klar. Viel Spaß noch. :-)")

