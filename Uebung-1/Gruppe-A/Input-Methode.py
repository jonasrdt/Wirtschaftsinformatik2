
print("-------------------------------------")
print("Wilkommen beim Pizzabestellprogramm.")
print("-------------------------------------")

# Festlegen des pauschalen Angebotspreises für eine Pizza
mittagsangebotspreis = 5

# Erfassen der User-Eingabe mit der input() Funktion
pizza = input("Bitte geben Sie den Namen der Pizza ein: ")
print("Ihre Eingabe lautet:", pizza)

menge = int(input("Wie viele Pizzen wollen Sie bestellen: "))
print("Sie haben", menge, "Mal", pizza, "Pizza bestellt.")
print("Die Gesamtbestellung kostet:", menge * mittagsangebotspreis, "€.")

