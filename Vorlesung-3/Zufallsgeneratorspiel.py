import random

zahl_1 = random.randint(1,10)
zahl_2 = random.randint(1,10)
loesung = zahl_1 + zahl_2

print("Willkommen zum Zufallsgeneratorspiel.")
print("Hier ist eine schwierige Mathe-Aufgabe für dich. Findest du die Lösung?")
print("Hier die Aufgabe:", zahl_1, "+", zahl_2)
user_loesung = int(input("Bitte gib hier deine Lösung ein: "))

if user_loesung == loesung:
    print("Glückwunsch! Das Ergebnis ist richtig:", user_loesung)
else:
    print("Das war leider falsch!")