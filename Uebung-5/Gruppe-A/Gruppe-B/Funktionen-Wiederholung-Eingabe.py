def zahleneingabe(zahlenart, datentyp):
    """
    The function zahleneingabe() takes two arguments, zahlenart and datentyp, and returns a number of
    the type datentyp
    
    :param zahlenart: This is the type of number you want to input
    :param datentyp: The type of number you want to input
    :return: the value of the variable zahl.
    """
    korrekte_eingabe = False
    while not korrekte_eingabe:
        try:
            zahl = datentyp(input("Bitte geben Sie die Zahl ein: "))
            korrekte_eingabe = True
            return zahl
        except:
            print("Bitte geben Sie nur", zahlenart ,"Zahlen ein.")


# Hauptprogramm
groesse_in_cm = zahleneingabe("Fließkommazahl", float)     # Fließkommazahl
gewicht_in_kg = zahleneingabe("Fließkommazahl", float)     # Fließkommazahl
alter = zahleneingabe("ganze", int)                        # Ganze Zahl