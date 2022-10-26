# while-Schleife, da Anzahl der Durchläufe nicht bekannt

# Definieren von korrekte_eingabe als Bool'sche Variable
korrekte_eingabe = False

while not korrekte_eingabe:
    # Abfangen von technischen Fehlern mittels try, except
    try:
        zahl = int(input("Bitte geben Sie eine ganze Zahl ein: "))
        print("Die eingegebene Zahl lautet", zahl)
        korrekte_eingabe = True
    except:
        print("Ihre Eingabe lautete", zahl, "und ist nicht korrekt.")
        print("Bitte geben Sie nur ganze Zahlen ein.")