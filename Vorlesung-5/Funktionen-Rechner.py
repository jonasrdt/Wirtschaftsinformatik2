# Erweitern Sie die folgende Python Funktion so, dass
# zwei Zahlen übergeben und die Summe zurückgegeben wird.

# Funktionsdefinition mit den Parametern 'zahl1' und 'zahl2'
def calculate(zahl1, zahl2):
    """
    The function "calculate" takes two numbers as input, adds them together, and prints the result.
    
    :param zahl1: The first number to be added in the calculation
    :param zahl2: The parameter "zahl2" is a variable that represents the second number that will be
    used in the calculation. It is passed as an argument to the "calculate" function along with another
    number represented by the parameter "zahl1"
    """
    # Variable 'ergebnis' ist nur im lokalen Kontext verfügbar
    ergebnis = zahl1 + zahl2
    print("Das Ergebnis für", zahl1, "+", zahl2, "lautet:", ergebnis, ".")


#### Hauptprogramm ####

# Ausführen der Funktion
calculate(5, 2)

print(ergebnis)