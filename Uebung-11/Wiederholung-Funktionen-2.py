

def zahl(platzhalter, datentyp):
    """
    It asks the user to enter a number, and returns the number if it's an integer or float
    
    :param platzhalter: This is the placeholder for the input
    :param datentyp: The type of data you want to return
    :return: the variable zahl.
    """
    richtige_eingabe = False
    while not richtige_eingabe:
        try:
            print("Bitte geben Sie", platzhalter, "ein.")
            zahl = datentyp(input("Eingabe: ")) # Lokale Variable, nicht von außen abrufbar!
            richtige_eingabe = True
        except:
            print("Bitte geben Sie nur ganze Zahlen ein.")
    return zahl


alter = zahl("Ihr Alter", int)
hausnummer = zahl("Ihre Hausnummer", int)

print("Das eingegebene Alter lautet: ", alter)
print("Die eingegebene Hausnummer lautet:", hausnummer)