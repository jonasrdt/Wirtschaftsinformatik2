import os

# Zuweisen des Verzeichnisses der Datei
aktuelles_Verzeichnis = os.path.dirname(__file__)

# Dateiname für Eingabe
dateiname = os.path.join(aktuelles_Verzeichnis, 'bibel.txt')

print("Der Dateipfad lautet: ", dateiname)

# Datei öffnen => Dateinamen + Modus (r/w)
datei = open(dateiname, 'r')

einzelne_woerter = []
gesamtlaenge = 0
anzahl_woerter = {}

# Ausgeben jeder einzelnen Zeile
for zeile in datei:
    replace = [",", ".", "#", "$", "§", "!", "?", "=", ")", "-", "(", ":", "'", ";", "1", "2", "3", "4", "5", "6", "7", "8", "9", "0", "\n"] 
    for element in replace:
        zeile = zeile.replace(element, "")
    # Alle Wörter in einer großen Liste erfassen
    einzelne_woerter.extend(zeile.split(" "))    
    # Länge der einzelnen Zeilen aufsummieren
    gesamtlaenge += len(zeile.replace(" ", ""))
    
# Zählen, wie oft ein einzelnes Wort vorkommt
for wort in einzelne_woerter:
    if wort in anzahl_woerter:
        anzahl_woerter[wort] +=1
    else:
        if wort != "" and len(wort) > 3 or wort == "Eva":
            anzahl_woerter[wort] = 1

datei.close()

# Dictionary nach Anzahl der Wörter sortieren
sortedList = sorted(anzahl_woerter.items(), key=lambda x: x[1], reverse=True)

# Dateiname für Ausgabe
dateiname = os.path.join(aktuelles_Verzeichnis, 'output.csv')

# Datei zum Schreiben öffnen
datei = open(dateiname, 'w')

for i in range(9000):
    datei.write(sortedList[i][0]+";"+str(sortedList[i][1])+"\n")
