# Entwickeln Sie mit Python eine Funktion, die bei Übergabe einer
# natürlichen Zahl n das Produkt 1*2*...*n berechnet und zurückgibt.

# Definition der Funktion fakultaet(zahl)
def fakultaet(zahl):
    """
    The function fakultaet takes a number as input and returns the factorial of that number
    
    :param zahl: The number you want to calculate the factorial of
    :return: the value of the variable fakultaet.
    """
    fakultaet = 1
    # Schleife für Durchläufe zur Berechnung der Fakultät
    for zaehler in range(1, zahl+1):
        # Die Variable Fakultät wird in jedem Durchlauf mit dem Zähler multipliziert
        fakultaet = fakultaet * zaehler
        print("Der aktuelle Wert beträgt:", fakultaet)
    return fakultaet

def zahleneingabe(zahlenart, datentyp):
    """
    The function zahleneingabe() takes two arguments, zahlenart and datentyp, and returns a number of
    the type datentyp
    
    :param zahlenart: This is the type of number you want to input
    :param datentyp: The type of number you want to input
    """
    korrekte_eingaben = False
    while not korrekte_eingaben:
        try:
            zahl = datentyp(input("Bitte geben Sie eine Zahl ein: "))
            korrekte_eingaben = True
        except:
            print("Bitte geben Sie nur", zahlenart ,"Zahlen ein.")
    return zahl

#################################
####### Hauptprogramm ###########
#################################

# Aufrufen der Funktion zahleneingabe()
zahl = zahleneingabe("natürliche", int)

# Aufrufen der Funktion fakultaet()
print("Die endgültige Fakultät beträgt:", fakultaet(zahl))