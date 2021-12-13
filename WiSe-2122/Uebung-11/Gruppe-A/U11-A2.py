# Entwickeln Sie eine Version von Hangman in Python. Hierbei soll randomisiert aus einer Liste von Ihnen
# vorgegebener Wörter eines ausgewählt und dem Nutzer zugewiesen werden. Dieser rät dann einzelne Buchstaben.
# Ist der Buchstabe korrekt, wird dieser in der nächsten Ausgabe an der richtigen Stelle angezeigt. Ist er nicht korrekt,
# verliert der Nutzer weiter Leben. Wenn Sie möchten, können Sie stattdessen auch versuchen ein Hangman-Männchen zu zeichnen.
import random

# Funktionsdefinition
def trenner(anzahl):
    for zaehler in range(anzahl):
        print("-", end="")
    print()

def successor():
    if "_" not in nutzer_wort:
        return True
    else:
        return False
    
def schwierigkeit():
    falsche_eingabe = True
    while falsche_eingabe:
        try:
            schwierigkeit = int(input("Bitte wähle deine Schwierigskeitstufe: (1) Schwer mit 3 Leben (2) Mittel mit 6 Leben (3) Einfach mit 9 Leben: "))
            if schwierigkeit == 1:
                falsche_eingabe = False
                return 3
            elif schwierigkeit == 2:
                falsche_eingabe = False
                return 6
            elif schwierigkeit == 3:
                falsche_eingabe = False
                return 9
            else:
                print("Deine Eingabe wurde leider nicht erkannt. Du startest mit der mittleren Stufe und 6 Leben.")
                falsche_eingabe = False
                return 6
        except:
            print("Bitte geben Sie nur Zahlen ein.")

# Variablendefinition
woerter = ["Fachhochschule", "Weihnachten", "Geschenke", "Silvester", "Betriebswirtschaftslehre", "Tee"]
zufaellige_zahl = random.randint(0, (len(woerter)-1))
gesuchtes_wort = woerter[zufaellige_zahl]
leben = 0
nutzer_wort = []

# Hauptprogramm
trenner(50)
print("Willkommen bei Hangman - Dem Wortratespiel")
leben = schwierigkeit()
print("Du startest jetzt mit",leben ,"Leben.")
print("Dein Wort hat:", len(gesuchtes_wort),"Zeichen.")
trenner(50)
for zaehler in range(len(gesuchtes_wort)):
    nutzer_wort.append("_")
print(nutzer_wort)

while leben > 0:    
    geratener_buchstabe = input("Bitte geben Sie einen Buchstaben ein: ")
    if geratener_buchstabe.upper() in gesuchtes_wort.upper():
        for char in range(len(gesuchtes_wort)):
            if gesuchtes_wort[char].upper() == geratener_buchstabe.upper():
                nutzer_wort.insert(char, geratener_buchstabe)
                nutzer_wort.pop(char+1)
        print(nutzer_wort)
        if successor():
            print("Herzlichen Glückwunsch. Du hast das Wort", gesuchtes_wort, "erfolgreich erraten.")
            break
    else:
        leben -= 1
        print("Schade, dieser Buchstabe kommt nicht vor.")
        print("Du hast noch", leben, "Versuche.")
        
if leben == 0:
    trenner(50)
    print("Das hat leider nicht geklappt. Das Lösungswort wäre:", gesuchtes_wort, "gewesen.")
    trenner(50)