# Einstieg in Funktionen

# 1. definieren der Funktion mit dem Namen trenner()
def trenner(anzahl_striche):
    for i in range(anzahl_striche):
        print("*", end="")
    print()

def abschluss():
    print("Ich bin fertig und das Programm wird beendet.")

def maximum_3_zahlen(zahl1, zahl2, zahl3):
    if zahl1 >= zahl2: # Ist die erste Zahl, die wir als Parameter eingegeben haben, größer als die zweite Zahl?
        maximum = zahl1 # Wenn das True ist, dann ist das maximum die erste Zahl
    else:
        maximum = zahl2 # Wenn die erste Zahl NICHT größer ist als die zweite, dann MUSS die zweite größer sein
    if maximum < zahl3: # Wenn der Gewinner des ersten Vergleichs KLEINER ist als die dritte Zahl, MUSS die dritte Zahl das Maximum sein
        maximum = zahl3
    return maximum # return gibt nur den Wert über die Funktion zurück, der danach verarbeitet muss





trenner(75)
# Der Nutzer wird gebeten drei Zahlen einzugeben
erste_zahl = int(input("Bitte geben Sie die erste Zahl ein: "))
zweite_zahl = int(input("Bitte geben Sie die zweite Zahl ein: "))
dritte_zahl = int(input("Bitte geben Sie die dritte Zahl ein: "))
trenner(75)

# Aufrufen der Funktion zum Vergleichen der drei Nutzereingaben
print("Das ermittelte Maximum beträgt:", maximum_3_zahlen(erste_zahl, zweite_zahl, dritte_zahl))
    