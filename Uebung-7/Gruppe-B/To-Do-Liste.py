# Schreiben Sie ein Programm, mithilfe dessen der User eine
# to-do Liste erstellen kann. Er soll hierbei Einträge verfassen
# und diese mit einer Priorität(1-99) speichern können.
# Achten Sie auf Fehleingaben durch den Nutzer.
# Der Nutzer kann solange to-dos eingeben, bis er "Nein" eingibt.

todoliste = []

weitere_eingabe = True
while weitere_eingabe:
    todo = input("Bitte geben Sie ein to-do ein: ")
    korrekte_eingabe = False
    while not korrekte_eingabe:
        try:
            prio = int(input("Bitte geben Sie die Priorität (1-99) ein: "))
            korrekte_eingabe = True
        except:
            print("Bitte geben Sie nur Zahlen ein:")
    
    todoliste.append([todo, prio])
    entscheidung = input("Wollen Sie eine weitere Eingabe tätigen (ja/nein): ")
    if entscheidung.lower() == "nein":
        weitere_eingabe = False

print(todoliste)

