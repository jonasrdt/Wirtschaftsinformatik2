import os
import csv

# Zuweisen des Verzeichnisses der Datei
aktuelles_Verzeichnis = os.path.dirname(__file__)

# Dateiname für Eingabe
dateiname = os.path.join(aktuelles_Verzeichnis, 'umsatz.csv')

dateioutput = os.path.join(aktuelles_Verzeichnis, 'output.csv')

print("Der Dateipfad lautet: ", dateiname)

with open(dateiname,'r') as csvinput:
    with open(dateioutput, 'w') as csvoutput:
        writer = csv.writer(csvoutput, lineterminator='\n')
        reader = csv.reader(csvinput)

        all = []
        for row in reader:
            row.append(';Berry')
            all.append(row)

        for row in reader:
            row.append(row[0])
            all.append(row)

        writer.writerows(all)
        