import random
random.seed()

richtige_eingabe = False
while not richtige_eingabe:
    try:
        wuerfelzahl = int(input("Bitte geben Sie Anzahl der Würfelseiten an: "))
        if wuerfelzahl <= 0:
            print("Bitte geben Sie nur Zahlen größer Null ein.")
        else:
            richtige_eingabe = True
    except:
        print("Bitte geben Sie nur ganze Zahlen ein.")

ergebnis = random.randint(1,wuerfelzahl)
print("Der Würfel mit", wuerfelzahl, "Seiten zeigt die Zahl", ergebnis,".")
