# Aufgabe 4 - Übung 4
# 
# Implementieren Sie einen einfachen Taschenrechner mit den Grundrechenoperationen (+- */).
# Sollten Sie bei der Grundrechenoperation ein q eingeben, dann endet das Programm.
# Bei allen anderen Grundrechenoperationen wird eine Fehlermeldung ausgegeben.

# Input des Nutzers für die Zahlen und die Rechenoperation erfassen
first_number = float(input("Bitte geben Sie die erste Zahl ein:"))

# Wird ein q eingegeben, endet der Taschenrechner
operator = input("Bitte geben Sie die Rechenoperation an, die Sie durchführen wollen:")
if operator == "q":
    exit()

second_number = float(input("Bitte geben Sie die zweite Zahl ein:"))

# Durchführen der Rechenoperation, entsprechend der Eingabe

if operator == "+":
    print(first_number, "+", second_number, "=", first_number + second_number)
elif operator == "-":
    print(first_number, "-", second_number, "=", first_number - second_number)
elif operator == "*":
    print(first_number, "*", second_number, "=", first_number * second_number)
elif operator == "/":
    print(first_number, "/", second_number, "=", first_number / second_number)
