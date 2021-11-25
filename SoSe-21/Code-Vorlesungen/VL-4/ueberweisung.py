
ungueltige_eingabe = True

while ungueltige_eingabe:
    try:
        ueberweisungsbetrag = float(input("Bitte geben Sie den Überweisungsbetrag an: "))
        if ueberweisungsbetrag < 50_000 and ueberweisungsbetrag > 0:
            print("Der von Ihnen angegebene Überweisungsbetrag lautet", ueberweisungsbetrag)
            print("Ihre Überweisung wird jetzt ausgeführt.")
            ungueltige_eingabe = False
        else:
            print("Der Überweisungsbetrag", ueberweisungsbetrag, "muss größer als 0 und kleiner als 50.000€ sein.")
    except:
        print("Ihre Eingabe war nicht gültig. Bitte geben Sie nur Zahlen an.")