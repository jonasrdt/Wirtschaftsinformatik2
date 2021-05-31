import os

# Variablen initialisieren
woerterCounter = 0
woerterDict = {}

# Zuweisen des Verzeichnisses der Datei
aktuelles_Verzeichnis = os.path.dirname(__file__)

# Dateiname für Eingabe
dateiname = os.path.join(aktuelles_Verzeichnis, 'bibel.txt')

print("Der Dateipfad lautet: ", dateiname)

# Datei öffnen
datei = open(dateiname, 'r')

# Datei auslesen
for zeile in datei:
    # Zeichen überspringen, die wir nicht mehr benötigen
    ueberspringe = [".", ",", ";", ":", "'", "(", ")", "-"]
    for char in ueberspringe:
        zeile = zeile.replace(char, "")
    zeile = zeile.lower()
    zeile = zeile.strip()
    # Alle Wörter in der Zeile trenne
    woerter = zeile.split(" ")
    # Zähle Wörter
    woerterCounter += len(woerter)
    # Anlegen des Dictionaries
    for wort in woerter:
        if wort in woerterDict:
            woerterDict[wort] +=1
        else:
            if wort != "" and len(wort) > 3:
                woerterDict[wort] = 1

datei.close()

# Dictionary nach Anzahl der Wörter sortieren
sortedList = sorted(woerterDict.items(), key=lambda x: x[1], reverse=True)

# Dateiname für Ausgabe
dateiname = os.path.join(aktuelles_Verzeichnis, 'output.csv')

# Datei zum Schreiben öffnen
datei = open(dateiname, 'w')
datei.write("Anzahl Wörter gesamt: " + str(woerterCounter)+"\n\n")
datei.write("Wort;Anzahl")
for i in range(3000):
    datei.write(sortedList[i][0]+";"+str(sortedList[i][1])+"\n")
datei.close()
