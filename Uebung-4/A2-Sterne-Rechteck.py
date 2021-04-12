# Aufgabe 2 - Übung 4
# 
# a.) Erstellen Sie ein Python-Programm, welches mittels zweier geeigneter Schleifen ein 20x5 großes Rechteck aus * erzeugt
# b.) Erweitern Sie Ihr Programm so, dass durch den Nutzer ein beliebiges Rechteck in x/y-Richtung erzeugt werden kann
# Tipp: Mit dem Zusatz end=" " verhindern Sie einen Zeilenumbruch bei der Ausgabe von print

x_Richtung = int(input("Wie viele in X-Richtung?"))
y_Richtung = int(input("Wie viele in Y-Richtung?"))

for zeilen in range(y_Richtung):
    for spalten in range(x_Richtung):
        print("*", end="")
    print()