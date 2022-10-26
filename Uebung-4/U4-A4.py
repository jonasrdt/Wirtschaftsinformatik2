# Implementieren Sie einen einfachen Taschenrechner mit den
# Grundrechenoperationen (+- */). Sollten Sie bei der Grundrechenoperation ein
# q eingeben, dann endet das Programm. Bei allen anderen Grundrechenoperationen
# wird eine Fehlermeldung ausgegeben.

# Abfrage der ersten Zahl und technische Fehlerprüfung mit try,except. while-Schleife
# läuft solange, bis der Nutzer eine gültige Zahl eingegeben hat.
korrekte_erste_eingabe = False
while not korrekte_erste_eingabe:
    try:
        # Erfassen der Zahl durch den Nutzer und umwandeln in den Datentypen float
        erste_zahl = float(input("Bitte geben Sie die erste Zahl ein: "))
        korrekte_erste_eingabe = True
    except:    
        print("Es ist ein Fehler aufgetreten. Bitte geben Sie nur Zahlen ein.")
        
# Abfrage der ersten Zahl und technische Fehlerprüfung mit try,except. while-Schleife
# läuft solange, bis der Nutzer eine gültige Zahl eingegeben hat.
korrekte_zweite_eingabe = False
while not korrekte_zweite_eingabe:
    try:
        # Erfassen der Zahl durch den Nutzer und umwandeln in den Datentypen float
        zweite_zahl = float(input("Bitte geben Sie die zweite Zahl ein: "))
        korrekte_zweite_eingabe = True
    except:    
        print("Es ist ein Fehler aufgetreten. Bitte geben Sie nur Zahlen ein.")

# Abfrage des Rechenoperators und inhaltliche Prüfung mit if,else
# while-Schleife läuft solange, bis der Nutzer einen gültigen Operator eingegeben hat.
korrekte_rechenoperation = False
while not korrekte_rechenoperation:
    rechenoperation = input("Bitte geben Sie eine Rechenoperation ein: ")
    if rechenoperation == "+" or rechenoperation == "-" or rechenoperation == "*" or rechenoperation == "/":
        korrekte_rechenoperation = True
    else:
        print("Bitte geben Sie nur + - / * ein.")

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