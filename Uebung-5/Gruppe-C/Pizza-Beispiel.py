# Entwickeln Sie ein Python-Programm, welches vergleicht, welcher
# Pizza-Durchmesser die größere Grundfläche hat.
# Frage: Bestelle ich eine 32cm Pizza oder 2 x 28cm Pizza (gemeint ist Durchmesser)?

# Globale Variablendefinition
pi = 3.1415


####### Funktionsdefinition ####### 
def grundflaeche(durchmesser, menge):
    grundflaeche = pi * ((durchmesser/2)**2) * menge
    return grundflaeche

def ganze_zahleneingabe(zweck):
    richtige_eingabe = False
    while not richtige_eingabe:
        try:    
            print("Bitte geben Sie eine Zahl ein für")
            ganze_zahl = int(input(zweck))
            richtige_eingabe = True
        except:
            print("Bitte geben Sie nur ganze Zahlen ein.")
    return ganze_zahl


####### Hauptprogramm ####### 
pizza_1 = ganze_zahleneingabe("Durchmesser Pizza 1: ")
pizza_2 = ganze_zahleneingabe("Durchmesser Pizza 2: ")

menge_1 = ganze_zahleneingabe("Menge Pizza 1: ")
menge_2 = ganze_zahleneingabe("Menge Pizza 2: ")

grundflaeche_pizza_1 = grundflaeche(pizza_1, menge_1)
grundflaeche_pizza_2 = grundflaeche(pizza_2, menge_2)

print("Die Grundfläche von Pizza 1 beträgt:", grundflaeche_pizza_1)
print("Die Grundfläche von Pizza 2 beträgt:", grundflaeche_pizza_2)
