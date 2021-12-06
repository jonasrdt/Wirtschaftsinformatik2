
# Entwickeln Sie eine Eingabemaske, in welche der Kunde einen Überweisungsbetrag
# eingeben und abschicken kann. Der Betrag soll auf seine Höhe geprüft werden (betrag > 0 and betrag <= 50.000).
# Außerdem sollen Fehleingaben durch den Nutzer abgefangen werden.

richtige_eingabe = False
kontostand = 2500

def trenner(anzahl):
    for zaehler in range(anzahl):
        print("-", end = "")
    print()

trenner(50)
print("Willkommen im Online-Banking der DKB.")
print("Ihr aktueller Kontostand beträgt: ", kontostand, "€.")
while not richtige_eingabe:
    try:
        betrag = float(input("Bitte geben Sie einen Überweisungsbetrag an: "))
        trenner(50)
        if betrag > 0 and betrag <= 50_000 and betrag <= kontostand:
            print("Der Betrag i.H.v.", betrag, "€ kann überwiesen werden.")
            print("Ihr neuer Kontostand beträgt:", kontostand - betrag, "€.")
            richtige_eingabe = True
        else:
            print("Bitte geben Sie einen gültigen Betrag ein, der größer als 0 aber kleiner als 50.000 ist und Ihren Kontostand i.H.v", kontostand, "€ nicht übersteigt.")
    except:
        print("Bitte geben Sie nur gültige Fließkommawerte an.")