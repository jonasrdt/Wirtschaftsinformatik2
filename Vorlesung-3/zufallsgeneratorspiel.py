# Dem Nutzer soll eine trivial Rechenaufgabe angezeigt werden,
# zu der er das Ergebnis eingibt. Anschließend soll geprüft werden,
# ob das Ergebnis korrekt ist. Wenn es nicht korrekt ist, soll das
# korrekte Ergebnis angezeigt werden.

import random
random.seed()

entscheidung = "ja"

while entscheidung.lower() == "ja":
    zahl_eins = random.randint(1, 6)
    zahl_zwei = random.randint(1,6)
    ergebnis = zahl_eins + zahl_zwei

    print("Bitte lösen Sie folgende Rechenaufgabe", zahl_eins, "+", zahl_zwei, "= ")
    
    for versuche in range(1,4):
        print("Das ist Ihr", versuche, "Versuch.")
        nutzereingabe = int(input("Bitte geben Sie das Ergebnis ein: "))
        
        if nutzereingabe == ergebnis:
            print("Sie sind ein toller Hecht.")
            break
        else:
            print("Das war leider nicht korrekt.")
            if versuche == 3:
                print("Schade, die Antworten waren bislang leider nicht korrekt.")
                print("Das Ergebnis lautet:", ergebnis, ".")
    
    entscheidung = input("Wollen Sie noch eine Aufgabe (ja/nein): ")
    