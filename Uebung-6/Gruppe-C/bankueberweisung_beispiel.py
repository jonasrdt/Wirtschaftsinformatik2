# Schreiben Sie ein Python-Programm, welches dem Nutzer die
# Eingabe einer Überweisungssumme ermöglicht. Es soll geprüft werden, ob das Limit von 5.000,00€
# überschritten wurde. Außerdem soll das Programm mögliche (technische) Eingabefehler des Nutzers abfangen.

ueberweisungslimit = 5_000

korrekte_eingabe = False
while not korrekte_eingabe:
    try:
        ueberweisung = float(input("Bitte geben Sie die Überweisungssumme ein: "))
        if 0 < ueberweisung < ueberweisungslimit:
            print("Die Überweisung i.H.v.", ueberweisung, "€ wird angewiesen.")
            korrekte_eingabe = True
        elif ueberweisung > ueberweisungslimit:
            print("Der von Ihnen eingegebene Betrag i.H.v.", ueberweisung, "€ überschreitet das Limit von 5.000,00€.")
        else:
            print("Bitte geben Sie nur positive Zahlen ein.")
    except:
        print("Bitte geben Sie nur Ganze oder Fließkommazahlen an.")

