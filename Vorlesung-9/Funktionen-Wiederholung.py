# Schreibe eine Funktion namens "berechne_benzinverbrauch", die
# den Benzinverbrauch eines Fahrzeugs basierend auf der gefahrenen Strecke
# und der Menge an verbrauchtem Benzin berechnet. Die Funktion sollte die beiden
# Parameter "strecke" und "benzinmenge" akzeptieren und den Benzinverbrauch in Litern
# pro 100 Kilometer zurückgeben.
# Verwende die folgende Formel, um den Benzinverbrauch zu berechnen:
# Benzinverbrauch = (benzinmenge / strecke) * 100


def berechne_benzinverbrauch(strecke, benzinmenge):
    verbrauch_pro_100km = round((benzinmenge / strecke) * 100, 2)
    return verbrauch_pro_100km

def fliesskommazahleneingabe(text, datentyp):
    korrekte_eingabe = False
    while not korrekte_eingabe:
        try:
            zahl = datentyp(input(text))
            korrekte_eingabe = True
        except:
            print("Bitte geben Sie nur Zahlen ein.")
    return zahl

benzinmenge = fliesskommazahleneingabe("Bitte geben Sie die Gesamtmenge an Benzin an: ", float)
strecke = fliesskommazahleneingabe("Bitte geben Sie die Anzahl der gefahrenen Kilometer an: ", float)

ergebnis = berechne_benzinverbrauch(strecke, benzinmenge)
print("Bei einer Strecke von:", strecke, "beträgt der Verbrauch pro 100km:", ergebnis, "Liter.")

