def addition(erste_zahl, zweite_zahl,dritte_zahl):
    """
    The function addition takes three numbers as input and prints the sum of the three numbers
    
    :param erste_zahl: This is the first parameter. It's the first number that the user will enter
    :param zweite_zahl: This is the second parameter. It's the second number that gets passed to the
    function
    :param dritte_zahl: This is the name of the parameter
    """
    # Ausgeben der loklane Variablen erste_zahl zweite_zahl dritte_zahl
    print("Es wurden die Zahlen", erste_zahl, "und", zweite_zahl, "und", dritte_zahl, "eingeben.")
    return erste_zahl + zweite_zahl + dritte_zahl

# Globale Variablen erste_zahl zweite_zahl dritte_zahl
erste_zahl = int(input("Bitte geben Sie die erste Zahl ein: "))
zweite_zahl = int(input("Bitte geben Sie die zweite Zahl ein: "))
dritte_zahl = int(input("Bitte geben Sie die dritte Zahl ein: "))

ergebnis = addition(erste_zahl, zweite_zahl, dritte_zahl)
print("Das Ergebnis der Funktion addition() hat ergeben: ", ergebnis)