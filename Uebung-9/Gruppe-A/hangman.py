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
leben = 6

trenner(50)
print("Willkommen beim Hangman-Spiel")
trenner(50)
print("Sie haben", leben, "Leben. Erraten Sie alle Buchstaben, bevor \nkeine Leben mehr vorhanden sind.")
buchstaben = input("Bitte geben Sie einen Buchstaben ein: ")
