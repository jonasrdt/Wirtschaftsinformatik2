# Aufgabe 4 - Übung 5
#
# Entwickeln Sie mit Python eine Funktion, die bei Übergabe einer
# natürlichen Zahl n das Produkt 1*2*...*n berechnet und zurückgibt.


# Abfangen von Fehleingaben, bspw. durch Buchstaben
gueltige_eingabe = False
while not gueltige_eingabe:
    try:
        # Eingabe des Nutzers erfassen
        natuerliche_zahl = int(input("Bitte geben Sie eine natürliche Zahl ein:"))
        print("Die von Ihnen eingegebene Zahl lautet:", natuerliche_zahl)
        gueltige_eingabe = True
    except:
        print("Bitte geben Sie nur Zahlen ein.")

def fakultaet(natuerliche_zahl):
    if natuerliche_zahl < 0:
        print("Fakultät von negativen Zahlen existiert nicht.")

    elif natuerliche_zahl == 0:
        return 1

    else:
        berechneter_wert = 1

        while natuerliche_zahl > 1:
            berechneter_wert *= natuerliche_zahl
            natuerliche_zahl -= 1
        return berechneter_wert

print (fakultaet(natuerliche_zahl))
