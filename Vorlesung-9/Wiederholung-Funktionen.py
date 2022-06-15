
# Funktionsdefinition mit der lokalen Variable ergebnis
def addition(zahl_1,zahl_2):
    """
    The function `addition` takes two numbers as input and returns their sum
    
    :param zahl_1: The first number to add
    :param zahl_2: The second number to add
    :return: The result of the addition of the two numbers.
    """
    ergebnis = zahl_1 + zahl_2
    # Globales Verfügbarmachen des Ergebnisses
    return ergebnis

def zahleneingabe(gesuchte_zahl, datentyp):
    """
    It asks the user to enter a number, and if the user enters a number, it returns that number.
    If the user enters something else, it asks the user to enter a number again
    
    :param gesuchte_zahl: The name of the number you're asking for
    :param datentyp: The data type you want the input to be
    :return: the input of the user.
    """
    richtige_eingabe = False
    while not richtige_eingabe:
        try:
            print("Bitte geben Sie", gesuchte_zahl, "ein.")
            zahl = datentyp(input("Eingabe: "))
            richtige_eingabe = True
            return zahl
        except:
            print("Bitte geben Sie nur ganze Zahlen ein.")


########################
##### Hauptprogramm ####
########################
alter = zahleneingabe("Ihr Alter", int)
hausnummer = zahleneingabe("Ihre Hausnummer", int)
groesse = zahleneingabe("Ihre Größe in Metern", float)
print("Ihr Alter beträgt", alter, "und Ihre Hausnummer lautet", hausnummer, "und Sie sind", groesse, "groß.")
