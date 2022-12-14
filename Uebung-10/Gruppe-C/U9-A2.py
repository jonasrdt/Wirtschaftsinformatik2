
import os

aktuelles_verzeichnis = os.path.dirname(__file__)

# Festlegen des Ausgangsdateipfads
ausgangsdateipfad = os.path.join(aktuelles_verzeichnis, 'umsatz.csv')

# Festlegen des Zieldateipfads
zieldateipfad = os.path.join(aktuelles_verzeichnis, 'umsatz_mod.csv')

# Öffnen der Ausgangsdatei, im Modus 'r' für read
ausgangsdatei = open(ausgangsdateipfad, 'r')

# Öffnen/Erstellen der Zieldatei, im Modus 'w' für write
zieldatei = open(zieldateipfad, 'w')

# Ergänzen eines Zeilenzählers mit dem Namen 'zeilennummer'
zeilennummer = 0

for zeile in ausgangsdatei:
    zeilennummer += 1
    zeile = zeile[:-1]
    if zeilennummer == 1:
        try:
            zieldatei.write(zeile + ";Provision\n")
            print("Zeile", zeilennummer, "wurde erfolgreich geschrieben.")
        except:
            print("Zeile", zeilennummer, "konnte nicht geschrieben werden.")
    elif zeilennummer >= 2:
        spalten = zeile.split(";")
        umsatz = float(spalten[1])
        if umsatz < 10_000:
            provision = umsatz * 0.25
        elif 10_000 < umsatz < 20_000:
            provision = umsatz * 0.30
        elif umsatz > 20_000:
            provision = umsatz * 0.35
        provision = round(provision, 2)
        try:
            zieldatei.write(zeile + ";" + str(provision) + "\n")
            print("Zeile", zeilennummer, "wurde erfolgreich geschrieben.")
        except:
            print("Zeile", zeilennummer, "konnte nicht geschrieben werden.")