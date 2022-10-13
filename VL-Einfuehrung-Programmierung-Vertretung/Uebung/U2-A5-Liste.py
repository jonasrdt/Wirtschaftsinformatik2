# Erstellen Sie ein Pgroesste_zahlthon-Programm das solange eine natürliche Zahl einliest,
# bis keine Zahl oder eine falsche Eingabe erfolgt. Am Ende soll die größte Zahl
# von den eingegebenen Zahlen auf der Konsole ausgegeben werden.

zahlen = []
abbruch = False
while not abbruch:
    try:
        natuerliche_zahl = int(input("Bitte geben eine Zahl größer oder gleich 0 ein: "))
        zahlen.append(natuerliche_zahl)
    except:
        if len(zahlen) == 0:
            print("Game Over.")
            print("Es konnte keine größte Zahl ermittelt werden.")
            abbruch = True
        else:
            print(f"Die größte Zahl ist {max(zahlen)}")
            abbruch = True


