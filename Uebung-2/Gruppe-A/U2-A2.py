
# Erstellen Sie ein Python Programm, mithilfe dessen Sie aus einem
# eingegeben Nettobetrag den Mehrwertsteuerbetrag (19%) und den
# Bruttobetrag errechnen sollen.

mehrwertsteuersatz = 0.19

# Definieren der Variable 'nettobetrag' durch Nutzereingabe und
# ändern des Datentyps auf float (Fließkommazahl)
nettobetrag = float(input("Bitte gib den Nettobetrag ein: "))
print("Der eingegebene Nettobetrag lautet:", nettobetrag, "€.")

# Definieren der Variable 'meherwertsteuerbetrag' durch
# Multiplikation des Nettobetrags mit dem Mehrwertsteuersatz
mehrwertsteuerbetrag = nettobetrag * mehrwertsteuersatz
print("Der erreechnete Mehrwertsteuerbetrag beträgt:", mehrwertsteuerbetrag, "€.")

# Definieren der Variable 'bruttobetrag' durch
# Addition von Nettobetrag und Mehrwertsteuerbetrag
bruttobetrag = nettobetrag + mehrwertsteuerbetrag
print("Der errechnete Bruttobetrag beträgt:", bruttobetrag, "€.")