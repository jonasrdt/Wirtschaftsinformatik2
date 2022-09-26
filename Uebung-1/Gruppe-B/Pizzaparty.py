# Schreiben Sie ein Programm, mithilfe dessen eine Pizza bestellt
# deren Menge angegeben und der Gesamtpreis berechnet werden kann.
# Die Pizza kostet im Mittagsangebot immer 5,00€

# Definition der Variable mittagsangebotspreis, um den Preis der Pizza fest zu speichern
# Datentyp Float (float)
mittagsangebotspreis = 5.00

# Erfassen des User Inputs für den Namen der Pizza und speichern als String (str)
pizza = input("Bitte geben Sie den Namen der Pizza ein, die Sie bestellen wollen: ")
print("Sie haben folgende Pizza bestellt:", pizza)

# Erfassen des User Inputs für die Menge der Pizzen und speichern als Integer (int)
menge = int(input("Bitte geben Sie an wieviele Pizzen Sie bestellen wollen: "))
print("Sie haben", menge, "Mal", pizza, "Pizza bestellt.")

# Berechnen des Gesamtpreises und speichern als Variable vom Typen Float (float)
gesamtpreis = menge * mittagsangebotspreis

print("Der Gesamtpreis beträgt:", gesamtpreis, "€.")

