# Das Zufallsgenerator-Spiel soll eine zufällige Rechenaufgabe
# vorschlagen, welche dann durch den Nutzer gelöst gewerden soll.
# Hierbei prüft das Programm, ob der Nutzer die richtige Antwort eingegeben hat
# und gibt ein entsprechendes Feedback.

# Import und Initialisierung des Moduls Random
import random
random.seed()

# Definieren einer Variable für den Schleifendurchlauf
richtige_antwort = False

# It generates two random numbers between 1 and 10.
zufallszahl_1 = random.randint(1, 10)
zufallszahl_2 = random.randint(1, 10)

# Ausgabe der Aufgabe
aufgabe = print("Die Aufgabe lautet:", zufallszahl_1, "+", zufallszahl_2)

# Berechnung des Ergebnisses
ergebnis = zufallszahl_1 + zufallszahl_2

while not richtige_antwort:
    # Erfassen der Antwort des Nutzers
    nutzerantwort = int(input("Bitte geben Sie das Ergebnis ein: "))
    # Prüfen des Ergebnisses
    if (ergebnis == nutzerantwort):
        print("Das Ergebnis", ergebnis, "ist korrekt. Herzlichen Glückwunsch.")
        richtige_antwort = True
    else:
        print("Das Ergebnis ist falsch.")