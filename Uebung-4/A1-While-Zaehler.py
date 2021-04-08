# Aufgabe 1 - Übung 4
#
# Eingabe
a = int(input("Erste Zahl: "))
b = int(input("zweite Zahl: "))

# Verarbeitung
zaehler = 0
while a >= b:
    a=a-b
    print (a)
    zaehler = zaehler + 1
    print("Der Zähler steht jetzt bei:", zaehler)
    print()
# Ausgabe
print("Zähler:", zaehler)