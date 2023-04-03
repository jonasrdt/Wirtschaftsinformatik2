# Entwickele ein Zufallsgenerator Spiel, welches dem User
# immer wieder unterschiedliche Rechenaufgabe ausgibt
# und prüft, ob die richtige Lösung eingegeben wurde.
import random

zahl_1 = random.randint(1, 10)
zahl_2 = random.randint(1, 10)
loesung = zahl_1 + zahl_2

print("##########################################")
print("Willkommen bei dem Zufallsgenerator-Spiel")
print("##########################################")
print("Bitte löse folgende Mathe-Aufgabe: ", zahl_1, "+", zahl_2)
user_loesung = float(input("Bitte geben Sie hier Ihre Lösung ein: "))

if user_loesung == loesung:
    print("Herzlichen Glückwunsch. Die Lösung", loesung, "ist richtig.")
else:
    print("Sie haben", user_loesung, "eingegeben.")
    print("Richtig gewesen wäre:", loesung)