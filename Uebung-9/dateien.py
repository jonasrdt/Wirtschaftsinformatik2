import os

# aktuelles Verzeichnis der Datei
aktVerzeichnis = os.path.dirname(__file__)

# Texte liegen z. B. im Unterverzeichnis /texte
txtVerzeichnis = os.path.join(aktVerzeichnis, 'texte')

# Dateiname
dateiname = os.path.join(txtVerzeichnis, 'bibel.txt')

# Datei öffnen
datei = open(dateiname, 'r')

# Erstelle ein Wörter-Dictionary
woerterDict = {}
woerterCount = 0

# Datei auslesen
for zeile in datei:
    # Wandle Zeile von Grossbuchstaben in klein um
    ueberspringe = [".", ", ", ":", ";", "'", '"', "(", ")", "-"]
    for char in ueberspringe:
        zeile = zeile.replace(char, "")
    zeile = zeile.lower()
    zeile = zeile.strip()
    # Alle Wörter in der Zeile trennen
    woerter = zeile.split(" ")
    # Zähle Wörter
    woerterCount += len(woerter)
    for wort in woerter:
        if wort in woerterDict:
            woerterDict[wort] += 1
        else:
            if wort != "" and len(wort) > 2:
                woerterDict[wort] = 0

datei.close()

# def returnValue(mylist):
#    return mylist[1]


# Dictionary nach Anzahl Wörtern sortieren
sortedList = sorted(woerterDict.items(), key=lambda x: x[1], reverse=True)

# Dateiname
dateiname = os.path.join(txtVerzeichnis, 'beispiel_output.csv')

# Datei zum schreiben öffnen
datei = open(dateiname, 'w')
datei.write("Anzahl Wörter gesamt: " + str(woerterCount)+"\n\n")
datei.write("Wort;Anzahl\n")
for i in range(50):
    datei.write(sortedList[i][0]+";"+str(sortedList[i][1])+"\n")

datei.close()
