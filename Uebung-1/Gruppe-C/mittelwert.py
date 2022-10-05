# Ändern Sie das Programm so ab, dass der Nutzer die drei Zahlen eingibt
# und daraus der Mittelwert errechnet wird.

# Abfrage der Zahlen durch den User und umwandeln (casten) in den Datentypen Float (float)
erste_zahl = float(input("Bitte geben Sie die erste Zahl ein: \t"))
zweite_zahl = float(input("Bitte geben Sie die zweite Zahl ein: \t"))
dritte_zahl = float(input("Bitte geben Sie die dritte Zahl ein: \t"))

# Berechnung des Mittelwerts auf Basis der vom User eingegebenen Zahlen
# und runden auf zwei Nachkommastellen
mittelwert = round((erste_zahl + zweite_zahl + dritte_zahl) / 3, 2)

# Ausgabe des Mittelwertes und der vom User eingegebenen Zahlen
print("Der Mittelwert der Zahlen:", erste_zahl, zweite_zahl, dritte_zahl, "lautet:", mittelwert)