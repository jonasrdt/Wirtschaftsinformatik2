

def mittelwertzweierzahlen(zahl1, zahl2):
    """
    The function calculates the average of two given numbers and returns the result.
    
    :param zahl1: The first number that will be used to calculate the average
    :param zahl2: The parameter 'zahl2' is a variable that represents the second number that will be
    used to calculate the average (or mean) with the first number ('zahl1') in the
    'mittelwertzweierzahlen' function
    :return: the average (or mean) of two numbers, which is calculated by adding the two numbers and
    dividing the sum by 2.
    """
    # Definieren der lokalen Variable 'mittelwert'
    mittelwert = (zahl1 + zahl2) / 2
    # Wiedergeben/Herausgeben des Wertes für 'mittelwert'
    return mittelwert

# Ausführen der Funktion im Hauptprogramm
ergebnis = mittelwertzweierzahlen(5, 10)
print(ergebnis)

