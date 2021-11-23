# Labor Übung 4 Nummer 5
# Implementieren Sie die Wuzelberechnung mit dem Newton-Verfahren. Sie sollen beliebige vom Nutzer eingegebene Werte berechenen können.
# Beachten Sie, dass aus negativen Werten per Definition keine Wurzel gezogen werden kann!
# Mit dem Newton-Verfahren nähert man sich der Wurzel von x mithilfe eines Startwers z durch Wiederholen der folgenden Berechnung an:
# z'= z-(z²-x)/2z
# Vielen Dank an Frau Spaett, die diese Aufgabe bereitstellt.


# Variabel zuordnen + Datentyp ändern in Float, Dezimalzahlen
x = float(input("Bitte geben Sie eine Zahl ein: "))
z = float(input("Bitte geben Sie eine Zahl ein: "))
# Delta definiert
delta = 0.0000001
# Zähler auf Null setzen
zaehler = 0
# Variabel der Formel zuordnen
z_strich = z-((z**2-x)/(2*z))
# If Funktion damit keine negativer Wert aus einer Wurzel gezogen wird
if x< 0:
    print("Aus negativen Werten kann per Definition keine Wurzel gezogen werden.")
else:
    # While Schleife läuft solange bis delta größer ist
    while abs(z_strich - z) > delta:
        z_strich = z
        z = z_strich - ((z_strich**2-x)/(2*z_strich))               
        zaehler=zaehler+1

# Ausgabe        
print("Ich musste hierzu", zaehler, "Iterationen durchführen.")
print( "Python behauptet die Wurzel von", x, "sei", z)
