
# Definieren (def) einer Funktion mit dem Namen "trenner"
def trenner(anzahl_sterne):
    for _ in range(anzahl_sterne):
        print("*", end="")
    print()

# Definieren (def) einer Funktion mit dem Namen "abschluss" die den Abschluss des Programms darstellt
def abschluss():
    print("Ich bin fertig.")

# Definieren der Funktion
def maximum_3_zahlen(zahl1, zahl2, zahl3):
    if zahl1 >= zahl2: # Ist die erste Zahl, die wir als Parameter eingeben haben, größer als die zweite Zahl?
        maximum = zahl1 # Wenn das True ist, ist das maximum erstmal die erste Zahl
    else:
        maximum = zahl2 # Wenn die erste Zahl NICHT größer ist als die zweite, dann MUSS die zweite größer sein
    if maximum < zahl3: # Wenn der Gewinner des ersten Vergleichs KLEINER ist als die dritte Zahl, MUSS die dritte Zahl das Maximum sein
        maximum = zahl3
    return maximum # return gibt nur den Wert über die Funktion zurück, der dann noch verarbeitet werden muss


trenner(10)
# Nutzer bitten drei Zahlen einzugeben
erste_zahl = int(input("Bitte geben Sie die erste Zahl ein:"))
zweite_zahl = int(input("Bitte geben Sie die zweite Zahl ein:"))
dritte_zahl = int(input("Bitte geben Sie die dritte Zahl ein:"))
trenner(10)

# Aufrufen der Funktion zum Vergleichen der drei Nutzereingaben
print("Das ermittelte Maximum beträgt:", maximum_3_zahlen(erste_zahl, zweite_zahl, dritte_zahl))
