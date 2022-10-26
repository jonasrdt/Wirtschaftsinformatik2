# Implementieren Sie einen einfachen Taschenrechner mit den
# Grundrechenoperationen (+- */). Sollten Sie bei der Grundrechenoperation ein
# q eingeben, dann endet das Programm. Bei allen anderen Grundrechenoperationen
# wird eine Fehlermeldung ausgegeben.

# Erfassen der Zahlen durch den Nutzer und umwandeln in den Datentypen float
erste_zahl = float(input("Bitte geben Sie die erste Zahl ein: "))
# Datentyp String für die Variable rechenoperation
rechenoperation = input("Bitte geben Sie die Rechenoperation ein: ")
# Erfassen der Zahlen durch den Nutzer und umwandeln in den Datentypen float
zweite_zahl = float(input("Bitte geben Sie die zweite Zahl ein: "))


# Prüfen ob die Rechenoperation zu einer der vorliegenden passt
if rechenoperation == "+":
    ergebnis = erste_zahl + zweite_zahl
elif rechenoperation == "-":
    ergebnis = erste_zahl - zweite_zahl
elif rechenoperation == "*":
    ergebnis = erste_zahl * zweite_zahl
elif rechenoperation == "/":
    ergebnis = erste_zahl / zweite_zahl
    # … wird ein q eingegeben, endet das Programm.
elif rechenoperation == "q":
    print("Sie haben ein q eingegeben. Das Programm endet jetzt.")
    # … wenn keiner der vorherigen Auswahlmöglichkeiten passt.
else:
    print("Ihre Eingabe passt leider zu keiner der Auswahlmöglichkeiten.")
    
# Prüfen, ob die Rechenoperation != q ist und bedingtes Ausführen
if rechenoperation != "q":
    print("Bei der Rechnung", erste_zahl, rechenoperation, zweite_zahl, "lautet das Ergebnis:", ergebnis)