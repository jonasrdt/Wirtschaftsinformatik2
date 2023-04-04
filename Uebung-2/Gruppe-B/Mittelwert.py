# Entwickeln Sie ein Python-Programm, welches aus drei eingegebenen
# Zahlen den Mittelwert bestimmt und ausgibt.

zahl_1 = float(input("Bitte gib die erste Zahl ein: "))
zahl_2 = float(input("Bitte gib die zweite Zahl ein: "))
zahl_3 = float(input("Bitte gib die dritte Zahl ein: "))

mittelwert = round((zahl_1 + zahl_2 + zahl_3) / 3, 2) 

print("Der errechnete Mittelwert beträgt:", mittelwert)