import os


aktuelles_Verzeichnis = os.path.dirname(__file__)
dateiname = os.path.join(aktuelles_Verzeichnis, "duplicates.txt")

# Datei öffnen
datei = open(dateiname, "r")

test = []
for zeile in datei:
    test.append(zeile)

print(len(test))