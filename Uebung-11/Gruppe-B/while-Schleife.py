

# while-Schleife läuft immer so lange,
# wie die mit ihr verknüpfte Bedingung Wahr ist
# while-Schleifen brauchen eine Abbruchbedingung

# Schreiben Sie eine while-Schleife die solange durchläuft
# bis der Nutzer eine 5 eingibt.
zahl = 0
while zahl != 5:
    print("Die Zahl lautet:", zahl)
    zahl = int(input("Wenn Sie abbrechen wollen, geben Sie eine 5 ein: "))
    

# Ergänzen Sie den nachfolgenden Code so, dass im Falle einer
# Fehleingabe durch den Nutzer – beispielsweise durch die Eingabe von Buchstaben –
# die Nachricht `"Bitte geben Sie nur Zahlen ein."` ausgegeben wird. Dies soll
# solange geschehen, bis der Nutzer eine korrekte Eingabe tätigt.

korrekte_eingabe = False
while not korrekte_eingabe:
    try:
        alter = int(input("Bitte geben Sie Ihr Alter ein: "))
        korrekte_eingabe = True
    except:
        print("Bitte geben Sie nur Zahlen ein.")