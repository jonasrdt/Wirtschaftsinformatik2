
# Definition einer Funktion mit dem Paramter "anzahl" für
# die Anzahl der anzuzeigenden Striche und "trennzeichen" für
# das Trennzeichen
def trenner(anzahl, trennzeichen):
    for zaehler in range(anzahl):
        print(trennzeichen, end= "")
    print()

# Definition einer Funktion zur Zahleneingabe und Wiedergabe mit return
def zahleneingabe():
    richtige_eingabe = False
    while not richtige_eingabe:
        try:
            zahl = int(input("Bitte geben Sie eine Zahl ein: "))
            richtige_eingabe = True
        except:
            print("Bitte geben Sie nur Zahlen ein.")
    return zahl

# Aufruf der Funktion trenner() mitsamt Parameter
trenner(15, "*")
alter = zahleneingabe()
print("Ihr Alter beträgt:", alter)
trenner(15, "*")
groesse = zahleneingabe()
print("Ihre Größe beträgt:", groesse)
trenner(15, "*")
