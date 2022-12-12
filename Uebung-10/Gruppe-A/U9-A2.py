# It imports the os module.
import os

# Laden des aktuellen Verzeichnisses
aktuelles_verzeichnis = os.path.dirname(__file__)

# Erstellen des Dateipfads der Ausgangsdatei
ausgangsdateipfad = os.path.join(aktuelles_verzeichnis, 'umsatz.csv')

# Erstellen des Dateipfads der Zieldatei
zieldateipfad = os.path.join(aktuelles_verzeichnis, 'umsatz_mod.csv')

# Öffnen der Ausgangsdatei im Modus read = 'r'
ausgangsdatei = open(ausgangsdateipfad, 'r')

# Öffnen der Datei zum Schreiben im Modus write = 'w'
zieldatei = open(zieldateipfad, 'w')

# Initialisieren der Zeilennummer
zeilennummer = 0

for zeile in ausgangsdatei:
    zeile = zeile[:-1]
    zeilennummer += 1 
    if zeilennummer == 1:
        zieldatei.write(zeile + ";Provision\n")
    elif zeilennummer >= 2:
        spalten = zeile.split(";")
        umsatz = int(spalten[1])
        if umsatz < 10_000:
            provision = umsatz * 0.25
        elif 10_000 <= umsatz <= 20_000:
            provision = umsatz * 0.30
        elif umsatz > 20_000:
            provision = umsatz * 0.35
        provision = round(provision, 2)
        try:
            zieldatei.write(zeile + ";" + str(provision).replace(".", ",") + "\n")
            print("Die Zeile", zeilennummer, "wurde erfolgreich geschrieben.")
        except Exception as error:
            print("Die Zeile", zeilennummer, "konnte nicht geschrieben werden.")
            print("Fehler:", error)