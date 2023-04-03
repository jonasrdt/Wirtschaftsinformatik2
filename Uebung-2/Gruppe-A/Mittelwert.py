# Schreiben Sie ein Programm, das den Mittelwert
# aus drei durch den User eingegebenen Zahlen errechnet,
# auf zwei Nachkommastellen rundet und anschließend ausgibt.

zahl_1 = float(input("Bitte geben Sie die erste Zahl ein: "))
zahl_2 = float(input("Bitte geben Sie die zweite Zahl ein: "))
zahl_3 = float(input("Bitte geben Sie die dritte Zahl ein: "))

mittelwert = round((zahl_1 + zahl_2 + zahl_3) / 3, 2)

print("Der Mittelwert beträgt:", mittelwert)