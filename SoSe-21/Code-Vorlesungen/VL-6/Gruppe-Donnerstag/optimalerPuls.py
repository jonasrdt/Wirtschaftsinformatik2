# Aufgabe 3 - Übung 5 
#
# Der optimale Puls bei Ausdauersportarten hängt vom Alter ab. Er lässt sich mit der Formel
# P = 165 - 0.75 * Alter
# bestimmen. Schreiben Sie ein Programm, das folgenden Dialog ermöglicht:
# Alter: 18
# optimaler Puls: 151.5
# Bringen Sie die Berechnung der Formel in eine Funktion!


# Funktionsdefinition für die Pulsberechnung mit dem Parameter "alter"
def berechnePuls(alter):
    puls_berechnung = 165 - 0.75 * alter
    return puls_berechnung

# Funktionsdefinition für das Einlesen des Alters ohne Parameter
def alterEinlesen():
    eingabeKorrekt = False
    while not eingabeKorrekt:
        try:
            alter = int(input("Bitte geben Sie Ihr Alter ein:"))
            eingabeKorrekt = True
        except:
            print("Das war leider keine gültige Eingabe.")
    return alter

# Funktionsdefinition, um den bereits zuvor in berechnePuls(alter) berechneten Puls + Alter auszugeben, mit den Parametern "alter" und "puls"
def gebeOptimalerPulsAus(alter, puls):
    print("Bei einem Alter von:", alter, "liegt Ihr optimaler Puls für Ausdauersportarten bei:", puls)

# Funktionsdefinition für die komplette EVA des Puls-Programms, ohne Parameter
def pulsBerechnung():
    alter = alterEinlesen()
    optimalerPuls = berechnePuls(alter)
    gebeOptimalerPulsAus(alter, optimalerPuls)


# Mithilfe dieses Funktionsaufrufs wird alles erledigt. Von Alter bis Berechnung.
pulsBerechnung()