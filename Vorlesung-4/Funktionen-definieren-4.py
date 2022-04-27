import math

def fakultaet(zahl):
    ergebnis = math.factorial(zahl)
    return ergebnis

richtige_eingabe = False
while not richtige_eingabe:
    try:
        zahl = int(input("Bitte geben Sie eine ganze Zahl ein: "))
        if zahl <= 0:
            print("Bitte geben Sie nur Zahlen größer als 0 ein.")
        else:
            richtige_eingabe = True
    except:
        print("Bitte geben Sie nur Zahlen ein.")

print("Das Ergebnis lautet:", fakultaet(zahl))

