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
    
def loesungsermittlung(anzahl_versuche, loesung):
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
    rechenoperationen = ["+", "-", "/", "*"]
    korrektes_rechenverfahren = False
    while not korrektes_rechenverfahren:
        rechenverfahren = input("Bitte geben Sie die Rechenoperation ein, die Sie durchführen wollen (+,-,/,*): ")
        if rechenverfahren in rechenoperationen:
            return rechenverfahren
        else:
            print("Bitte geben Sie nur +, -, /, * ein: ")
  

def rechenaufgabe(operator, erste_zahl, zweite_zahl):
       print("Die Aufgabe lautet:", erste_zahl, operator, zweite_zahl)
       aufgabe = str(erste_zahl) + operator + str(zweite_zahl)
       loesung = eval(aufgabe)
       return loesung
       

spielentscheidung = True
while spielentscheidung:
    erste_zahl = random.randint(1,15)
    zweite_zahl = random.randint(1,15)
    loesungsermittlung(anzahl_versuche, rechenaufgabe(rechenverfahren(), erste_zahl, zweite_zahl))
    weiterspielen = input("Wollen Sie weiterspielen (ja/nein): ")
    if weiterspielen.lower() == "nein":
        spielentscheidung = False
        print("Alles klar. Viel Spaß noch. :-)")

