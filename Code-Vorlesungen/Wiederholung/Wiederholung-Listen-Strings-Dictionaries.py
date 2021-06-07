a = "Das ist ein String"
b = ["Das", "ist", "eine", "Liste"]
c = ["Mehrere", "Datentypen", 5.3, True]
d = {"Berlin": 3_500_000,
     "Kiel": 255_000}

# Einen String mithilfe von split() in eine Liste überführen
a_splitted = a.split(" ")
# Mithilfe von len() die Länge der Liste ermitteln
print(len(a_splitted))
# Ermitteln der durchschnittlichen Wortlänge
wortlaenge = len(a) / len(a_splitted)
print("Die Wörter sind durchschnittlich", wortlaenge, "Zeichen lang.")

# Verschachtelung zu einer Liste hinzufügen
print(b)
b.append(["Liste", "in", "der", "Liste"])
print(b)
# Auf ein bestimmtes Element einer Liste innerhalb einer Liste zugreifne
print(b[4][0])

