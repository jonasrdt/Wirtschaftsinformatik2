# Initialisierung der stueckliste
stueckliste = []

def teilhinzufuegen(position, bestandteil, menge):
    stueckliste.append([])
    stueckliste[position-1].append(bestandteil)
    stueckliste[position-1].append(menge)

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
    print ("Bitte geben Sie die Menge für das", i , "Teil der Stückliste an:")
    menge = input()
    teilhinzufuegen(i, bestandteil, menge)

print("Hier sind die Teile Ihrer Stückliste:", stueckliste) 