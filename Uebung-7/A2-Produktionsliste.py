# Initialisierung der stueckliste
stueckliste = []

def teilhinzufuegen(bestandteil):
    stueckliste.append(bestandteil)

def trenner(anzahl):
    for i in range(anzahl):
        print("*", end="")
    print()

trenner(125)
print("Programm zur Erfassung der Stückliste für das SpaceX Starship")
korrekte_eingabe = False
while not korrekte_eingabe:
    try:
        menge = int(input("Wie viele Teile wollen Sie der Stückliste hinzufügen? "))
        if menge <= 0:
            print("Bitte geben Sie eine ganze Zahl größer 0 ein.")
        else:
            korrekte_eingabe = True
    except:
        print("Bitte geben Sie eine ganze Zahl größer 0 ein.")
trenner(125)

for i in range (1, menge+1):
    print("Sie wollen", menge, "Teile erfassen.")
    print ("Bitte geben Sie das", i ,"Teil der Stückliste an:")
    bestandteil = input()
    teilhinzufuegen(bestandteil)

print("Hier sind die Teile Ihrer Stückliste:", stueckliste) 