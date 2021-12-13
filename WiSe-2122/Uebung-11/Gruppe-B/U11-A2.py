# Entwickeln Sie eine Version von Hangman in Python. Hierbei soll randomisiert aus einer Liste von Ihnen
# vorgegebener Wörter eines ausgewählt und dem Nutzer zugewiesen werden. Dieser rät dann einzelne Buchstaben.
# Ist der Buchstabe korrekt, wird dieser in der nächsten Ausgabe an der richtigen Stelle angezeigt. Ist er nicht korrekt,
# verliert der Nutzer weiter Leben. Wenn Sie möchten, können Sie stattdessen auch versuchen ein Hangman-Männchen zu zeichnen.
import random

### Funktionsdefinition
# Diese Funktion erzeugt schöne Trennstriche
def trenner(anzahl):
    for zaehler in range(anzahl):
        print("-", end="")
    print()
    
# Diese Funktion prüft, ob der vom Nutzer geratene Buchstabe mit einem der Buchstaben aus dem Wort übereinstimmt
def buchstaben_pruefung():
    for char in range(len(ausgewaehltes_wort)):
        if geratener_buchstabe.upper() == ausgewaehltes_wort[char].upper():
            gesuchtes_wort.insert(char, geratener_buchstabe)
            gesuchtes_wort.pop(char+1)
            
# Diese Funktion prüft, ob noch freie und zu besetzende Stellen in der Liste des gesuchten Wortes sind
def successor():
    if "_" not in gesuchtes_wort:
        return True
            
# Variablendefinition
woerter = ["Tee", "Wasser", "Fachhochschule", "Betriebswirtschaftslehre", "Python", "Weihnachten", "Silvester"]
gesuchtes_wort = []
leben = 6
# Erstellt eine zufällige Zahl, um zufällig ein Wort aus der o.g. Liste woerter zu entnehmen
zufaellige_zahl = random.randint(0, (len(woerter)-1))
ausgewaehltes_wort = woerter[zufaellige_zahl]

# Hauptprogramm
trenner(50)
print("Willkommen beim Hangman-Spiel - Dem Wortratespiel")
print("Ihnen wird jetzt zufällig ein Wort zugewiesen.")
print("Sie müssen durch die Eingabe einzelner Buchstaben das Wort Stück für Stück erraten.")
# Schwierigkeitsgrad bestimmen
falsche_eingabe = True
while falsche_eingabe:
    # Technische Fehlerabfrage mit try,except
    try:
        spielmodus = int(input("Welchen Spielmodus möchten Sie wählen: (1) schwierig mit nur 3 Leben (2) mittel mit 6 Leben und (3) für leicht mit 12 Leben: "))
        if spielmodus == 1:
            leben = 3
            falsche_eingabe = False
        elif spielmodus == 2:
            leben = 6
            falsche_eingabe = False
        elif spielmodus == 3:
            leben = 12
            falsche_eingabe = False
        else:
            print("Deine Eingabe war leider ungültig, du startest standardmäßig mit: ", leben, "Leben.")
            falsche_eingabe = False
    except:
        print("Bitte geben Sie nur ganze Zahlen zwischen 1 und 3 ein.")
trenner(50)
print("Zu Beginn hast du", leben, "Leben.")
trenner(50)
# Ausgeben der Länge des Wortes
print("Dein Wort hat", len(ausgewaehltes_wort),"Zeichen.")
# Initialisieren der Liste in der Länge des gesuchten Wortes
for zaehler in range(len(ausgewaehltes_wort)):
    gesuchtes_wort.append("_")
trenner(50)

# Die folgende Schleife läuft solange durch, wie der Nutzer entweder Leben
# oder aber bis er das Wort komplett richtig eraten hat. 
while leben > 0:
    geratener_buchstabe = input("Rate einen Buchstaben: ")
    buchstaben_pruefung()
    print(gesuchtes_wort)
    # Prüft, ob der geratene Buchstabe überhaupt in dem Wort vorkommt
    if geratener_buchstabe.upper() in ausgewaehltes_wort.upper():
        # Prüft, ob noch freie Stellen zu besetzen sind, oder das Wort damit abschließend erraten wurde
        if successor() == True:
            print("Herzlichen Glückwünsch, du hast gewonnen!")
            break
    else:
        leben -= 1
        print("Schade, das war leider nicht richtig. Du hast noch", leben, "Leben.")
    trenner(50)