
# Entwickeln Sie eine Eingabemaske, in welche der Kunde einen Überweisungsbetrag
# eingeben und abschicken kann. Der Betrag soll auf seine Höhe geprüft werden (betrag > 0 and betrag <= 50.000).
# Außerdem sollen Fehleingaben durch den Nutzer abgefangen werden.

richtige_eingabe = False

def trenner(anzahl):
    for zaehler in range(anzahl):
        print("-", end = "")
    print()

trenner(50)
print("Willkommen im Online-Banking der DKB.")
while not richtige_eingabe:
    try:
        betrag = float(input("Bitte geben Sie einen Überweisungsbetrag an: "))
        trenner(50)
        if betrag > 0 and betrag <= 50_000:
            print("Der Betrag i.H.v.", betrag, "€ kann überwiesen werden.")
            richtige_eingabe = True
        else:
            print("Bitte geben Sie einen gültigen Betrag ein, der größer als 0 aber kleiner als 50.000 ist.")
    except:
        print("Bitte geben Sie nur gültige Fließkommawerte an.")