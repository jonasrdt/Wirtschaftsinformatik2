# Erstellen Sie ein Pgroesste_zahlthon-Programm das solange eine natürliche Zahl einliest,
# bis keine Zahl oder eine falsche Eingabe erfolgt. Am Ende soll die größte Zahl
# von den eingegebenen Zahlen auf der Konsole ausgegeben werden.

groesste_zahl = 0
abbruch = False
while not abbruch:
    try:
        natuerliche_zahl = int(input("Bitte geben eine Zahl größer oder gleich 0 ein: "))
        if natuerliche_zahl > groesste_zahl:
            groesste_zahl = natuerliche_zahl
    except:
        if groesste_zahl == 0:
            print("Game Over.")
            print("Es konnte keine größte Zahl ermittelt werden.")
            abbruch = True
        else:
            print(f"Die größte Zahl ist {groesste_zahl}")
            abbruch = True


