

nummernliste = []
abbruchbedingung = False
while not abbruchbedingung:
    try:
        zahl = int(input("Bitte geben Sie eine natürliche Zahl ein: "))
        nummernliste.append(zahl)
    except:
        abbruchbedingung = True
nummernliste.sort()
print(nummernliste)
print("Die Liste hat:", len(nummernliste), "Elemente.")
print("An erster Stelle steht:", nummernliste[0])
print("An letzter Stelle steht:", nummernliste[-1], "und ist somit auch die größte Zahl.")
