# Aufgabe 4 - Übung 4
# 
# Implementieren Sie einen einfachen Taschenrechner mit den Grundrechenoperationen (+- */).
# Sollten Sie bei der Grundrechenoperation ein q eingeben, dann endet das Programm.
# Bei allen anderen Grundrechenoperationen wird eine Fehlermeldung ausgegeben.

# Erste Eingabe einer Zahl
gueltige_erste_eingabe = False
while not gueltige_erste_eingabe:
    try:
        first_number = float(input("Bitte geben Sie die erste Zahl ein:"))
        gueltige_erste_eingabe = True
    except:
        print("Bitte geben Sie ausschließlich Zahlen ein.")

gueltiger_operator = False
while not gueltiger_operator:
    operator = input("Bitte geben Sie die Rechenoperation ein:")
    if operator == "+" or operator == "-" or operator == "/" or operator == "*":
        gueltiger_operator = True
    elif operator == "q":
        exit() # bricht jedes Python Programm sofort ab
    else:
        print("Bitte einen der folgenden Operatoren verwenden + - / *:")

# Zweite Eingabe einer Zahl
gueltige_zweite_eingabe = False
while not gueltige_zweite_eingabe:
    try:
        second_number = float(input("Bitte geben Sie die zweite Zahl ein:"))
        gueltige_zweite_eingabe = True
    except:
        print("Bitte geben Sie ausschließlich Zahlen ein.")

# Durchführen der Rechenoperation, entsprechend der Eingabe
if operator == "+":
    print(first_number, "+", second_number, "=", first_number + second_number)
elif operator == "-":
        print(first_number, "-", second_number, "=", first_number - second_number)
elif operator == "*":
        print(first_number, "*", second_number, "=", first_number * second_number)
elif operator == "/":
        print(first_number, "/", second_number, "=", first_number / second_number)