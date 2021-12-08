richtige_eingabe = False

while not richtige_eingabe:
    try:
        # Inhaltliche Prüfung der Variablen
        a = int(input("Bitte geben Sie eine Zahl ein: "))
        b = int(input("Bitte geben Sie eine zweite Zahl ein: "))
        if a > b:
            print(a, "ist größer als", b)
            richtige_eingabe = True
        elif a == b:
            print(a, "ist genau so groß wie", b)
            richtige_eingabe = True
        elif a < b:
            print(a, "ist nicht größer als", b)
            richtige_eingabe = True
        else:
            print("Es konnte kein mathematischer Vergleich angestellt werden.")
    except:
        print("Es handelt sich hierbei scheinbar nicht um Zahlen.")