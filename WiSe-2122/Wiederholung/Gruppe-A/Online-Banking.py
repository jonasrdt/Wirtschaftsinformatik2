
# Programmieren Sie eine Eingabemaske, über welche der Nutzer einen Überweisungsbetrag eingeben kann.
# Dieser soll auf Gültigkeit geprüft werden: betrag > 0 and betrag <= 50000
# Achten Sie hierbei auf das Abfangen von Fehleingaben.

# Ergänzen Sie das Programm anschließend so, dass ein Kontostand vorgegeben
# und geprüft wird, ob die Überweisung durchgeführt werden kann. Anschließend
# soll der Kontostand aktualisiert und ausgegeben werden.

def trenner(anzahl):
    for zaehler in range(anzahl):
        print("-", end="")
    print()

kontostand = 2_500
gueltige_eingabe = False

while not weitereueberweisung:
    trenner(50)
    print("Willkommen beim DKB Online Banking.")
    while not gueltige_eingabe:
        trenner(50)
        betrag = float(input("Bitte geben Sie Ihren Überweisungsbetrag ein: "))
        trenner(50)
        try:
            if betrag > 0 and betrag <= 50_000 and betrag <= kontostand:
                print("Der Betrag i.H.v.", betrag, "€ wurde erfolgreich überwiesen.")
                print("Ihr neuer Kontostand beträgt: ", kontostand - betrag, "€.")
                gueltige_eingabe = True
                trenner(50)
            else:
                print("Bitte geben Sie einen Betrag ein der größer als 0, kleiner als 50.000 und Ihren Kontostand i.H.v.", kontostand,"€ nicht überschrietet.")
        except:
            print("Bitte geben Sie eine gültige Fließkommazahl an.")