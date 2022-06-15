# Einfache Überprüfung des Alters mithilfe von if/else
richtige_eingabe = False
while not richtige_eingabe:
    try:
        alter = int(input("Bitte geben Sie Ihr Alter ein: "))
        if alter <= 0:
            print("Bitte geben Sie ein Alter größer 0 ein.")
        else:
            richtige_eingabe = True
    except:
        print("Bitte geben Sie nur ganze Zahlen ein: ")
print("Das von Ihnen eingegebene Alter beträgt:", alter)


# Bedeutung von Elif für Betrachtung der gesamten Kontrollstruktur
bmi = 30
if bmi < 21:
    print("21")
elif bmi > 25:
    print("25")
elif bmi > 30:
    print("30")
else:
    print("else")