# Entwickeln Sie eine Version von Hangman in Python. Hierbei soll randomisiert aus einer Liste
# von Ihnen vorgegebener Wörter eines ausgewählt und dem Nutzer zugewiesen werden.
# Dieser rät dann einzelne Buchstaben. Ist der Buchstabe korrekt, wird dieser in der nächsten
# Ausgabe an der richtigen Stelle angezeigt. Ist er nicht korrekt, verliert der Nutzer weiter
# Leben. Wenn Sie möchten, können Sie stattdessen auch versuchen ein Hangman-Männchen
# zu zeichnen.

def trenner(anzahl):
    for i in range(anzahl):
        print("-", end="")
    print()

# Variablendefinition
wort = "Python"
placeholder = [] 
leben = 6
errateneBuchstaben = 0
vollstaendig = False

# Hauptprogramm
trenner(50)
print("Willkommen beim Hangman-Spiel")
trenner(50)
print("Sie haben", leben, "Leben. Erraten Sie alle Buchstaben, bevor \nkeine Leben mehr vorhanden sind.")
print("Das zu erratene Wort hat", len(wort), "Zeichen.")

while not vollstaendig:
    buchstabe = input("Bitte geben Sie einen Buchstaben ein: ")
    for char in range(len(wort)):
        if wort[char].lower() == buchstabe.lower():
            print("Sie haben den Buchstaben", buchstabe, "richtig erraten.")
            errateneBuchstaben += 1
            break
        else:
            print("Der Buchstabe", buchstabe, "ist nicht in dem Wort vorhanden.")
            print("Sie verlieren ein Leben.")
            leben -= 1
            print("Sie haben jetzt noch", leben, "Leben.")
            
    if errateneBuchstaben == len(wort):
        vollstaendig = True
        print("Herzlichen Glückwunsch, Sie haben das Wort", wort, "erraten.")