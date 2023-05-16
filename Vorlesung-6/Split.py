
# Passen Sie folgenden Code so an, dass aus dem vorliegenden
# String eine Liste mit einzelnen Elementen erstellt wird

satz = "Manche Leuchten, wenn man sie liest."
print("Der Satz, wie er vorher war:", satz)
satz_split = satz.split(" ")
print("Der Satz, nachdem wir .split() angewendet haben:", satz_split)

# Geben Sie aus, wie viele Wörter in dem Satz vorkommen
laenge_liste = len(satz_split)
print("Die Liste ist", laenge_liste, "Elemente lang.")


# Schreiben Sie eine Funktion, welche die Länge einer übergebenen Liste ermittelt
def listenlaenge(liste):
    listenlaenge = len(liste)
    return listenlaenge

# Schreiben Sie eine Funktion, welche einen übergebenen Satz in eine Liste splittet
def listengenerator(satz):
    satz_split = satz.split(" ")
    return satz_split

