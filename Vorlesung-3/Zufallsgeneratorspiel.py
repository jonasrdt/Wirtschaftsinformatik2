import random

zahl_1 = random.randint(1,10)
zahl_2 = random.randint(1,10)
loesung = zahl_1 + zahl_2
# Definieren der Variable 'richtige_antwort' vom Datentypen Boolean
richtige_antwort = False

print("Willkommen zum Zufallsgeneratorspiel.")
print("Hier ist eine schwierige Mathe-Aufgabe für dich. Findest du die Lösung?")
print("Hier die Aufgabe:", zahl_1, "+", zahl_2)

while not richtige_antwort:
    user_loesung = int(input("Bitte gib hier deine Lösung ein: "))
    if user_loesung == loesung:
        print("Glückwunsch! Das Ergebnis ist richtig:", user_loesung)
        richtige_antwort = True
    else:
        print("Das war leider falsch!")