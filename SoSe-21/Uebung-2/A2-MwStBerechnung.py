# Aufgabe 2 - Übung 2
# 
# Erstellen Sie ein Python-Programm mit den folgenden Anforderungen:
# Es soll aus einem eingegebenen Nettobetrag die 19% Mehrwertsteuer und der Bruttobetrag errechnet und angezeigt werden.

# 1. Statische Variablen festlegen
mwst = 0.19

# 2. Nutzereingabe erfassen und in float umwandeln
nettobetrag = float(input("Bitte geben Sie den Nettobetrag ein:"))
print ("Der von Ihnen eingegebene Nettobetrag ist:", nettobetrag, "€.")

# 3. Mehrwertsteuerbetrag errechnen und ausgeben
mehrwertsteuerbetrag = nettobetrag * mwst
print("Der Mehrwertsteuerbetrag beträgt:", mehrwertsteuerbetrag, "€.")

# 4. Bruttobetrag errechnen und ausgeben
bruttobetrag = nettobetrag + mehrwertsteuerbetrag
print("Der Bruttobetrag beträgt:", bruttobetrag, "€.")