import os

# # Variablen initialisieren
woerterCounter = 0
zeichenCounter = 0
woerterDict = {}

# Zuweisen des Verzeichnisses der Datei
aktuelles_Verzeichnis = os.path.dirname(__file__)

# Dateiname für Eingabe
dateiname = os.path.join(aktuelles_Verzeichnis, 'bibel.txt')

print("Der Dateipfad lautet: ", dateiname)

# Datei öffnen
datei = open(dateiname, 'r')

for zeile in datei:
    # Bereinigen der Zeile um alle Elemente aus der Liste replace[]
    replace = ["#", "'", "!", "?", ",", ";", ".", "§", "(", ")", "[", "]", ":", "1", "2", "3", "4", "5", "6", "7", "8", "9", "0", "\n"]
    for element in replace:   
        # Zeile bereinigen
        zeile = zeile.replace(element, "")
    # Zählen der Wörter
    liste = []
    liste = zeile.split(" ")
    woerterCounter += len(liste)
    # Zählen der Zeichen
    zeichenCounter += len(zeile)
    
    for wort in liste:
        if wort in woerterDict:
            woerterDict[wort] += 1
        else:
            if len(wort) > 3 and wort != "" or wort == "Eva":
                woerterDict[wort] = 1
                
datei.close()

# Dictionary nach Anzahl der Wörter sortieren
sortedList = sorted(woerterDict.items(), key=lambda x: x[1], reverse=True)

# Dateiname für Ausgabe
dateiname = os.path.join(aktuelles_Verzeichnis, 'output.csv')

# Datei zum Schreiben öffnen
datei = open(dateiname, 'w')

for i in range(9000):
    try:
        datei.write(sortedList[i][0]+";"+str(sortedList[i][1])+"\n")
        print("Juhuu Zeile erfolgreich geschrieben.")
    except:
        print("Datei zu schreiben hat nicht geklappt.")