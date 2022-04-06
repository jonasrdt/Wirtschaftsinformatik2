# Das Zufallsgenerator-Spiel soll eine zufällige Rechenaufgabe
# vorschlagen, welche dann durch den Nutzer gelöst gewerden soll.
# Hierbei prüft das Programm, ob der Nutzer die richtige Antwort eingegeben hat
# und gibt ein entsprechendes Feedback.

# Importieren des Moduls "random", um zufällige Zahlen zu generieren
import random
random.seed()

weitermachen = True

while weitermachen:
    # Generieren von zwei Zufallszahlen und speichern in zahl_1 und zahl_2
    zahl_1 = random.randint(1, 10)
    zahl_2 = random.randint(1, 10)

    # Ausgeben der Aufgabe
    print("Die Aufgabe lautet:", zahl_1, "+", zahl_2, "=")

    # Berechnung des Ergebnisses
    ergebnis = zahl_1 + zahl_2

    # Dem Nutzer werden drei Versuche zur Beantwortung der Aufgabe gewährt
    for versuche in range(1,4):
        # Nutzereingabe
        nutzereingabe = int(input("Bitte geben Sie das Ergebnis ein: "))
        # Ergebnis vergleichen mit Nutzereingabe
        if nutzereingabe == ergebnis:
            print("Ihr Ergebnis", nutzereingabe, "ist korrekt.")
            nutzer_entscheidung = input("Willst du noch eine Aufgabe (ja/nein): ")
            if nutzer_entscheidung.lower() == "nein":
                weitermachen = False
            break # Bricht die Schleife automatisch ab
        else:
            # Wenn alle drei Versuche unerfolgreich verspielt wurden, hat der Nutzer verloren.
            if versuche == 3:
                print("Sie haben alle Versuche verbraucht. Schade.")
            else:
                print("Leider ist das Ergebnis falsch. Das war Ihr", versuche, "Versuch.")
