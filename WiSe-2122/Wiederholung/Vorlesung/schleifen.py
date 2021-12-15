

# for - Schleife
# läuft für eine fest vorgebene Anzahl von Durchläufen

for zeilen in range(1,11):
    print("Zeile Nr.", zeilen, end=" ")
    for spalten in range(1,11):
        print("_", end =" ")
    print()

# while - Schleife
# läuft solange, bis eine Abbruchbedingung eintritt

falsche_aussage = True

while falsche_aussage:
    aussage = input("Hat der Gärtner seine Frau umgebracht (ja/nein): ")
    if aussage.lower() == "ja":
        print("Das war die richtige Aussage. Sie dürfen gehen.")
        falsche_aussage = False # Abbruchbedingung
    else:
        print("Bitte nicht lügen, es ist immer der Gärtner.")
    