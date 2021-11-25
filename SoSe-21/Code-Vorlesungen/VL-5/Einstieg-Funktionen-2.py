# Definieren meiner Funktion
# # Als erstes: def
# # Als zweites: Name der Funktion
# # Gefolgt von ():
def trenner(anzahl_sterne):
    for i in range(anzahl_sterne):
        print("*", end="")
    print()

# Diese Funktion berechnet die größte Zahl aus drei eingegebenen Zahlen
def berechnung_maximum(zahl1, zahl2, zahl3):
    if zahl1 >= zahl2: # Ist die erste Zahl, die wir als Parameter eingegeben haben, größer als die zweite Zahl?
        maximum = zahl1
    else:  
        maximum = zahl2 # Wenn die erste Zahl NICHT größer ist als die zweite, dann MUSS die zweiter größer sein
    if maximum < zahl3:
        maximum = zahl3 # Wenn der Gewinner des ersten Vergleichs KLEINER ist als die dritte Zahl, muss die dritte Zahl das Maximum sein
    return maximum # return gibt nur den Wert über die Funktion zurück, der dann noch verarbeitet werden muss

trenner(35)
print("Geben Sie drei Zahlen ein und es wird Ihnen die größte Zahl zurückgegeben.")
trenner(35)
erste_zahl = int(input("Bitte geben Sie die erste Zahl ein:"))
zweite_zahl = int(input("Bitte geben Sie die zweite Zahl ein:"))
dritte_zahl = int(input("Bitte geben Sie die dritte Zahl ein:"))
trenner(35)

# Aufrufen der Funktion
print("Die größte Zahl ist:", berechnung_maximum(erste_zahl, zweite_zahl, dritte_zahl))

