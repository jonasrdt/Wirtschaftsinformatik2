
# Erzeugen Sie eine Ausgabe, die nur den Vornamen "Bob" ausgibt
satz = "Recherchen und Archiv: Bob Andrews"

# Klassisches Zählen und dann slicen
print(satz[23:26])

# Wissen, dass das B nur einmal in dem Satz vorkommt
# Index herausfinden, als Untergrenze festlegen
# und Index + 3 als Obergrenze nehmen, da "Bob"
# drei Zeichen lang ist
print(satz[satz.index("B"):satz.index("B")+3])

# Splitten der Liste und suchen nach dem Wort,
# welches mit "Bob" übereinstimmt
satz_splitted = satz.split(" ")
for wort in satz_splitted:
    if wort == "Bob":
        print("Bob kommt an Stelle:", satz_splitted.index(wort), "in der Liste vor.")
