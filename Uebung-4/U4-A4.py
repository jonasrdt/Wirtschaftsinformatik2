# Implementieren Sie einen einfachen Taschenrechner mit den
# Grundrechenoperationen (+- */). Sollten Sie bei der Grundrechenoperation ein
# q eingeben, dann endet das Programm. Bei allen anderen Grundrechenoperationen
# wird eine Fehlermeldung ausgegeben.

# Erfassen der Zahlen durch den Nutzer und umwandeln in den Datentypen float
erste_zahl = float(input("Bitte geben Sie die erste Zahl ein: "))
zweite_zahl = float(input("Bitte geben Sie die zweite Zahl ein: "))

# Datentyp String für die Variable rechenoperation
rechenoperation = input("Bitte geben Sie die Rechenoperation ein: ")

if rechenoperation == "+":
    ergebnis = erste_zahl + zweite_zahl
elif rechenoperation == "-":
    ergebnis = erste_zahl - zweite_zahl
elif rechenoperation == "*":
    ergebnis = erste_zahl * zweite_zahl
elif rechenoperation == "/":
    ergebnis = erste_zahl / zweite_zahl

print("Bei der Rechnung", erste_zahl, rechenoperation, zweite_zahl, "lautet das Ergebnis:", ergebnis)
