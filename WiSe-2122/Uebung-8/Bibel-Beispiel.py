# Text der Bibel lesen, Wörter zählen und als CSV ausgeben
import os

# Variablen initialisieren
woerterCounter = 0
woerterDict = {}

# Zuweisen des Verzeichnisses der geöffneten Datei
aktuelles_Verzeichnis = os.path.dirname(__file__)
print("Wir befinden uns in dem Verzeichnis: ", aktuelles_Verzeichnis)

# Dateinamen für das Einlesen zusammenführen
dateiname = os.path.join(aktuelles_Verzeichnis, "bibel.txt")
print("Der Dateipfad der Bibel.txt lautet: ", dateiname)

# Datei öffnen
datei = open(dateiname, "r")

# Datei auslesen und Zeile für Zeile bearbeiten
for zeile in datei:
    # Definition aller Zeichen, welche entfernt werden mögen
    ueberspringe = [".", ",", ";", ":", "'", "(", ")", "-", "#", "§", "!" , "\n", "1", "2", "3", "4", "5", "6", "7", "8", "9", "0"]
    # Schleife zum Prüfen jedes Chars jeder einzelnen Zeile
    for character in ueberspringe:
        zeile = zeile.replace(character, "")
    # Maßnahmen zur Vereinheitlichung der Zeichenkette
    zeile = zeile.lower()
    zeile = zeile.strip()
    # Überführen der Zeichenkette (str) in eine Liste (list)
    woerter = zeile.split(" ")
    # Zählen der Anzahl der Wörter der aktuellen Zeile und hinzufügen zum Counter
    woerterCounter += len(woerter)
    # Durch die Liste woerter iterieren
    for wort in woerter:
        # Prüfen, ob das Wort bereits im Dictionary vorhanden ist
        if wort in woerterDict:
            woerterDict[wort] += 1
        else:
            # Prüfen, dass wort nicht leer und größer als drei Zeichen ist
            if wort != "" and len(wort) > 3 and wort != "sein" and wort != "mein":
                woerterDict[wort] = 1

# Datei wieder schließen
datei.close()

# Dateinamen für die Ausgaben vorbereiten
dateiname = os.path.join(aktuelles_Verzeichnis, "bibel_output.csv")

# Überführen des Dictionaries in eine Liste und Sortieren
sortedList = sorted(woerterDict.items(), key=lambda x: x[1], reverse= True)

# Datei zum Schreiben öffnen
datei = open(dateiname, "w")

# Anzahl der Wörter übermitteln
datei.write("Anzahl aller Wörter gesamt: " + str(woerterCounter)+"\n\n")
# Tabellentitel festlegen und durch ; trennen
datei.write("Wort;Anzahl")
# Die ersten 3000 Elemente ausgeben in der Kombination KEY ; VALUE
for zaehler in range(3000):
    datei.write(sortedList[zaehler][0] + ";" + str(sortedList[zaehler][1])+"\n")
datei.close()