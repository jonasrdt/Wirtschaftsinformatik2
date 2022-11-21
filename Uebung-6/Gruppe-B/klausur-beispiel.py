liste = [["Paris", 782913],         # Index 0
         ["Kiel", 24618949]]        # Index 1 

# Ergänzen Sie den Code so, dass die Stadt Athen mit 5.223.100 Einwohner ergänzt wird
liste.append(["Athen", 5_223_100]) # Index 2

# Schreiben Sie eine for-Schleife, welche nur die Städtenamen ausgibt
for stadt in liste:
    print(stadt[0])
