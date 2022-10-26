# Schreiben Sie ein Python-Programm, welches dem Nutzer
# die Eingabe einer Überweisungssumme ermöglicht.
# Es soll geprüft werden, ob das Limit von 5.000,00€ überschritten wurde.
# Außerdem soll das Programm mögliche (technische) Eingabefehler des Nutzers abfangen.

korrekte_eingabe = False
while not korrekte_eingabe:
    try:
        ueberweisungssumme = float(input("Bitte geben Sie die Überweisungssumme an: "))
        print("Die Überweisungssumme beträgt", ueberweisungssumme, "€.")
        if ueberweisungssumme > 5_000:
            print("Sie haben Ihren Verfügungsrahmen überschritten. Bitte geben Sie eine kleinere Zahl ein.")
        else:
            print("Die Überweisung i.H.v.", ueberweisungssumme, "€ wurde ausgeführt.")
            korrekte_eingabe = True
    except:
        print("Sie haben keine Zahl eingegeben. Bitte erneut versuchen.")

