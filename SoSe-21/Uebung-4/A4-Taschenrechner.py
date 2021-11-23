# Aufgabe 4 - Übung 4
# 
# Implementieren Sie einen einfachen Taschenrechner mit den Grundrechenoperationen (+- */).
# Sollten Sie bei der Grundrechenoperation ein q eingeben, dann endet das Programm.
# Bei allen anderen Grundrechenoperationen wird eine Fehlermeldung ausgegeben.

falsche_eingabe = True

while falsche_eingabe:
    try:
        # Input des Nutzers für die Zahlen und die Rechenoperation erfassen
        first_number = float(input("Bitte geben Sie die erste Zahl ein:"))
        falsche_eingabe = False
    except:
        print("Bitte geben Sie nur Zahlen ein.")

falscher_operator = True
while falscher_operator:
    # Wird ein q eingegeben, endet der Taschenrechner
    operator = input("Bitte geben Sie die Rechenoperation an, die Sie durchführen wollen:")
    if operator == "+" or operator == "-" or operator == "/" or operator == "*":
        falscher_operator = False
    else:
        print("Bitte geben Sie einen gültigen Operator ein.")


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
