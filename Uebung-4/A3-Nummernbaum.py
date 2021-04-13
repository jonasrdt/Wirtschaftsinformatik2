# Aufgabe 3 - Übung 4
# 
# Erstellen Sie ein Python-Programm mit den folgenden Anforderungen:
# • Definieren Sie eine Zähl-Variable mit dem Wert 9
# • Erstellen Sie folgende Ausgabe

hoechsterWert = 9

for zeilen in range (hoechsterWert+1):
    # Leerzeichen generieren
    for werte in range (hoechsterWert+1-zeilen):
        print (" ", end=" ")
    # Hochzählen der Werte
    for werte in range (1, zeilen+1):
        print (werte, end=" ")
    # Vom höchsten Wert aus der vorherigen Schleife herunterzählen
    for werte in range (zeilen -1, 0, -1):
        print (werte, end=" ")
    print() 