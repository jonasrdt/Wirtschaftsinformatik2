# Entwickeln Sie eine Version von Hangman in Python. Hierbei soll randomisiert aus einer Liste von Ihnen
# vorgegebener Wörter eines ausgewählt und dem Nutzer zugewiesen werden. Dieser rät dann einzelne Buchstaben.
# Ist der Buchstabe korrekt, wird dieser in der nächsten Ausgabe an der richtigen Stelle angezeigt. Ist er nicht korrekt,
# verliert der Nutzer weiter Leben. Wenn Sie möchten, können Sie stattdessen auch versuchen ein Hangman-Männchen zu zeichnen.
import random

def trenner(anzahl):
    for i in range(anzahl):
        print("-", end="")
    print()
    
def successor():
    if "_" in gesuchtes_wort:
        return False
    else:
        return True
    
def spielmodus():
    falsche_eingabe = True
    while falsche_eingabe:
        try:
            modus = int(input("Wählen Sie eine Schwierigkeitsstufe: (1) Schwer - 3 Versuche (2) Mittel - 6 Versuchen (3) Einfach - 9 Versuchen: "))
            if modus == 1:
                falsche_eingabe = False
                return 3
            elif modus == 2:
                falsche_eingabe = False
                return 6
            elif modus == 3:
                falsche_eingabe = False
                return 9
            else:
                print("Ihre Schwierigkeit wird standardmäßig auf Mittel gesetzt.")
                falsche_eingabe = False
                return 6
        except:
            print("Bitte geben Sie nur ganze Zahlen ein.")

# Variablendefinition
words = ["Jessica", "Jonas", "Maike", "Milan", "Damla", "Merda", "Andre", "Sarangoo"]
# Alternative Lösung:
# print(random.choice(words))
zufaelliger_wert = random.randint(0,len(words)-1)
zufaelliges_wort = words[zufaelliger_wert]
gesuchtes_wort = []
versuche = 0

# Hauptprogramm
trenner(50)
print("Willkommen bei Hangman - Dem Wortratespiel")
print("Im Folgenden müssen Sie ein Wort erraten.")
versuche = spielmodus()
print("Dafür haben Sie",versuche,"Versuche.")
trenner(50)
print("Das von Ihnen zu erratene Wort hat", len(zufaelliges_wort), "Zeichen.")
for element in range(len(zufaelliges_wort)):
    gesuchtes_wort.append("_")
print(gesuchtes_wort)

while not successor() and versuche > 0:
    buchstabe = input("Bitte raten Sie einen Buchstaben: ")
    if buchstabe.upper() in zufaelliges_wort.upper():
        for char in range(len(zufaelliges_wort)):
            if buchstabe.upper() == zufaelliges_wort[char].upper():
                # Einfügen des Buchstaben am korrekten Index
                gesuchtes_wort.insert(char, buchstabe)
                # Entfernen des aufgeschobenen Platzhalters
                gesuchtes_wort.pop(char+1)
    else:
        versuche -= 1
        print("Schade, das war nicht richtig. Du hast noch", versuche,"Versuche.")
    print(gesuchtes_wort)
    if successor():
        print("Herzlichen Glückwunsch. Sie haben das Wort", zufaelliges_wort, "erraten.")

if versuche == 0:
    print("DUUUU HAST VERLOREN!")
    print("Das richtige Wort wäre gewesen:", zufaelliges_wort)