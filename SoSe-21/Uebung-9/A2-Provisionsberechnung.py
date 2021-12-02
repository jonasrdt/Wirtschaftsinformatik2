import os

# aktuelles Verzeichnis der Datei
aktVerzeichnis = os.path.dirname(__file__)

# Dateiname 1 zum Lesen
dateiname1 = os.path.join(aktVerzeichnis, 'umsatz.csv')

# Dateiname 2 zum Schreiben
dateiname2 = os.path.join(aktVerzeichnis, 'umsatz_mod.csv')

# Datei öffnen
datei1 = open(dateiname1, 'r')

# Datei zum Schreiben öffnen
datei2 = open(dateiname2, 'w')

# Zeilennummer merken
zeilennr = 0

# Zeilenweise Datei verarbeiten
for zeile in datei1:
    # Zeilenumbruch verhindern
    zeile = zeile[:-1]
    zeilennr += 1
    if zeilennr == 1:
        datei2.write(zeile + ";Provision\n")
    if zeilennr >= 2:
        spalten = zeile.split(";")
        umsatz = int(spalten[1])
        if umsatz < 10000:
            provision = umsatz * 0.25
        elif umsatz >= 10000 and umsatz <= 20000:
            provision = umsatz * 0.3
        else:
            provision = umsatz * 0.35
        provision = round(provision, 2)
        datei2.write(zeile + ";" + str(provision).replace(".", ",") + "\n")
    print("Die Zeile", zeilennr, "wurde erfolgreich geschrieben.")    

datei1.close()
datei2.close()
