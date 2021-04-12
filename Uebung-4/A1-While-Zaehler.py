# Aufgabe 1 - Übung 4
#
# Eingabe
a = int(input("Erste Zahl: "))
b = int(input("zweite Zahl: "))

# Verarbeitung
schleifenZaehler = 0
while a >= b:
    a=a-b
    print (a)
    schleifenZaehler = schleifenZaehler + 1
    print("Der Zähler steht jetzt bei:", schleifenZaehler)
    print()
# Ausgabe
print("Die Schleife ist:", schleifenZaehler, "Mal durchgelaufen.")