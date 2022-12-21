# Globale Variable mit Namen 'sonderzeichen'
sonderzeichen = [".", ",", "!", ";", ":", "?", "-", "_", "§", "$", "€", "&", "/", "(", ")", "=", " "]

# Eingabe eines Satzes durch den Nutzer
eingabe = input("Bitte geben Sie einen Satz ein: ")

# Ermitteln der Anzahl der Wörter, in dem der Satz (string) mithilfe von .split() in eine Liste
# überführt und deren Länge mithilfe von len() ermittelt wird
anzahl_woerter = len(eingabe.split(" "))

# Löschen aller Zeichen, welche sich in der Liste 'sonderzeichen' befinden, indem über die Liste iteriert wird
for zeichen in sonderzeichen:
    eingabe = eingabe.replace(zeichen, "")

# Ermitteln der durchschnittlichen Wortlänge, in dem die Anzahl der Zeichen durch die Anzahl der Wörter geteil wird
durchschnittliche_wortlaenge = round(len(eingabe) / anzahl_woerter,2)

print("Der bereinigte Satz lautet:", eingabe)
print(len(eingabe), "ist die Zeichenanzahl")
print("Der Satz beeinhaltet:", anzahl_woerter, "Wörter.")
print("Die durchschnittliche Wortlänge beträgt:", durchschnittliche_wortlaenge)