ueberweisungslimit = 50_000
kontostand = 3_500
ungueltiger_betrag = True

# Funktionsdefinition
def trenner(anzahl):
    for zaehler in range(anzahl):
        print("-", end="")
    print()

# Funktionsaufruf
trenner(50)
print("Willkommen beim Online-Banking der DKB")
print("Ihr Überweisungslimit beträgt", ueberweisungslimit, "€")
print("Ihr aktueller Kontostand beträgt", kontostand, "€")
trenner(50)
while ungueltiger_betrag:
    try:
        betrag = round(float(input("Bitte geben Sie einen Überweisungbetrag in € ein: ")),2)
        if betrag > ueberweisungslimit:
            print("Ihr Betrag liegt über den Überweisungslimit von", ueberweisungslimit, "€.")
        elif betrag < 0:
            print("Bitte geben Sie nur positive Zahle für eine Überweisung ein.")
        elif betrag > kontostand:
            print("Leider reicht Ihr Kontostand i.H.v.", kontostand,"€ nicht für die Überweisung i.H.v.", betrag,"€ aus.")
            entscheidung = input("Wollen Sie einen niedrigeren Betrag überweisen (ja/nein): ")
            if entscheidung.lower() == "nein":
                ungueltiger_betrag = False
        else:
            print("Ihre Überweisung i.H.v.", betrag,"€ wurde durchgeführt.")
            kontostand -= betrag
            print("Ihr neuer Kontostand beträgt:", kontostand, "€.")
            ungueltiger_betrag = False
    except:
        print("Bitte geben Sie nur Zahlen ein.")

