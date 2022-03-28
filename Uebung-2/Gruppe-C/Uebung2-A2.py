# Erstellen Sie ein Python-Programm mit den folgenden Anforderungen:
# Es soll aus einem eingegebenen Nettobetrag die 19% Mehrwertsteuer und der
# Bruttobetrag errechnet und angezeigt werden.

# Variablendefinition
mwst = 0.19

# Erfassen der Nutzereingabe und umwandeln von String in Float
nettobetrag = float(input("Bitte geben Sie einen Nettobetrag ein: "))
print("Der eingegebene Nettobetrag beträgt:", nettobetrag, "€.")

# Berechnung des Steuerbetrags auf Basis des Nettobetrags und 19% MwSt.
steuerbetrag = round(nettobetrag * mwst, 2)
print("Der Steuerbetrag für", nettobetrag, "€ beträgt:", steuerbetrag, "€ bei", mwst, "% MwSt.")

# Zusammenführen von Steuerbetrag und Nettobetrag zur Berechnung des Bruttobetrags
bruttobetrag = steuerbetrag + nettobetrag
print("Der Bruttobetrag beträgt:", bruttobetrag, "€.")
