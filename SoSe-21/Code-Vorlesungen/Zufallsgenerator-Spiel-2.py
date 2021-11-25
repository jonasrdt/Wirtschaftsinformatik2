# Zufallsgenerator Spiel
# v.0.2.
# Jonas Reinhardt

import random
random.seed()

# Spielentscheidung des Spielers
spielen = "JA"

while spielen.upper() == "JA":
    # Werte generieren
    a = random.randint(1,10)
    b = random.randint(1,10)
    
    # Lösung berechnen
    loesungAddition = a + b
    loesungMultiplikation = a * b

    # Spieler bekommt Aufgabe
    print ("")
    print ("Willkommen beim Zufallsgenerator Spiel.")
    entscheidung = input("Geben Sie 'a' ein für Addition oder 'm' für Multiplikation:")
    print ("")

    if entscheidung.upper() == "A":
        print ("Hier ist Ihre Aufgabe:", a, "+", b)
    elif entscheidung.upper() == "M":
        print ("Hier ist Ihre Aufgabe:", a, "*", b)

# Diese Schleife gibt dem Nutzer drei Versuche die richtige Antwort zu finden
    for versuch in range (1,4):
        # Spieler tätigt Eingabe der Antwort
        print(versuch, ". Versuch.")

        gueltige_eingabe = False
        while not gueltige_eingabe:
            try:
                tipp = int(input("Bitte geben Sie Ihren Tipp ein: "))
                gueltige_eingabe = True
            except:
                print("Ihre Eingabe war nicht gültig, bitte geben Sie eine Zahl ein.")

        # Prüfen, ob der Tipp des Spielers korrekt ist
        # Prüfen von Addition
        if entscheidung == "a":
            if tipp == loesungAddition:
                print ("Herzlichen Glückwunsch, Ihr Tipp:", tipp, "war richtig.")
                spielen = input("Wollen Sie weiterspielen (ja/nein)?")
                # break sorgt dafür, dass die for-Schleife beendet wird
                break 
            else:
                print ("Ihr Tipp:", tipp, "war leider nicht richtig.")
                if versuch == 3:
                    print ("Das richtige Ergebnis wäre:", loesungAddition)

        # Prüfen der Multiplikation
        elif entscheidung == "m":
            if tipp == loesungMultiplikation:
                print ("Herzlichen Glückwunsch, Ihr Tipp:", tipp, "war richtig.")
                spielen = input("Wollen Sie weiterspielen (ja/nein)?")
                # break sorgt dafür, dass die for-Schleife beendet wird
                break 
            else:
                print ("Ihr Tipp:", tipp, "war leider nicht richtig.")
                if versuch == 3:
                    print ("Das richtige Ergebnis wäre:", loesungMultiplikation)