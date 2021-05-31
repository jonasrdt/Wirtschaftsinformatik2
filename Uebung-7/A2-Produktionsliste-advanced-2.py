# Initialisierung der Stückliste
stueckliste = []

# Funktionsdefinition
def teilehinzufuegen(position, bestandteil, anzahl):
    stueckliste.append([])
    stueckliste[position-1].append(bestandteil)
    stueckliste[position-1].append(anzahl)


print("Bitte erfassen Sie im Folgenden die Teile für die Stückliste des SpaceX Starship.")

# Nutzereingabe der Menge
korrekte_eingabe = False
while not korrekte_eingabe:
    try:
        menge = int(input("Wie viele Teile wollen Sie hinzufügen: "))
        if menge <= 0:
            print("Bitte geben Sie eine ganze Zahl größer 0 ein.")
        else:
            print("Sie wollen", menge, "Teile hinzufügen.")
            korrekte_eingabe = True
    except:
        print("Bitte geben Sie nur Zahlen ein.")

# Verarbeitung des Nutzerinputs
# range(start, stop, step)
for teile in range(1, menge+1):
    print("Bitte geben Sie Teil", teile, "in der Liste an.")
    bestandteil = input("Bitte geben Sie den Namen des Teils ein: ")
    anzahl = int(input("Bitte geben Sie die Menge für das Teil ein: "))
    teilehinzufuegen(teile, bestandteil, anzahl)

# Ausgabe des verarbeiteten Nutzerinputs
print("Hier sind die Teile Ihrer Stückliste: ", stueckliste)