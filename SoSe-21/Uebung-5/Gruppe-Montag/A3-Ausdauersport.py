# Der optimale Puls bei Ausdauersportarten hängt vom Alter ab. Er lässt sich mit der Formel
# P = 165 - 0.75*Alter
# bestimmen. Schreiben Sie ein Programm, das folgenden Dialog ermöglicht:
# Alter: 18
# optimaler Puls: 151.5
# Bringen Sie die Berechnung der Formel in eine Funktion!

# Eingabe des Nutzers empfangen und auf Gültigkeit prüfen
gueltiges_alter = False
while not gueltiges_alter:
    try:
        alter = int(input("Bitte geben Sie Ihr Alter ein: "))
        if 6 <= alter <= 120:
            print("Das von Ihnen eingegebene Alter lautet:", alter)
            gueltiges_alter = True
        else:
            print("Bitte geben Sie ein gültiges Alter zwischen 6 und 120 ein.")
    except:
        print("Bitte geben Sie nur Zahlen ein.")

# Verarbeitung des optimalen Puls' für Ausdauersportarten auf Basis des eingegebenen Alters
def p(alter):
    puls = 165 - 0.75 * alter
    return puls

# Ausgabe der Werte
print("Ihr optimaler Puls für Ausdauersportarten beträgt:", p(alter))