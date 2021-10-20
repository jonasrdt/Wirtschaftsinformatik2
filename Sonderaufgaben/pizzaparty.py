# # # # Sonderaufgabe # # # # 
# Entscheiden Sie sich unter ökonomischen Gesichtspunkten:
# Kaufen Sie 3 Pizzen mit einem 26er Durchmesser
# oder lieber 2 Pizzen mit einem 34er Durchmesser?

# Gehen Sie bei der Betrachtung davon aus, dass beide Angebote
# insgesamt 20.49€ kosten.

Pi = 3.14159 # Globale Variable Pi zur Berechnung des Umfangs und der Fläche

# Definition der Funktion zur Berechnung des Kreisumfangs in Zentimetern einer Pizza auf Basis des Radius
def pizzaumfang(Radius):
    # Berechnung des Kreisumfangs und Runden auf 2 Nachkommastellen und Zuweisen des Ergebnisses zur lokalen Variable pizzaumfang
    pizzaumfang = round(2 * Pi * Radius, 2)
    # Verfügbarmachen des Wertes für den Kreisumfang aus dem lokalen Kontext in den globalen
    return pizzaumfang

# Berechnung der Grundfläche einer Pizza in Quadratzentimetern, basierend auf dem Radius und der Anzahl der Pizzen
def pizzaflaeche(Radius, Anzahl):
    # Berechnung der Grundfläche und Runden auf 2 Nachkommastellen und Zuweisen des Ergebnisses zur lokalen Variable pizzaflaeche
    pizzaflaeche = round(Pi * (Radius * Radius) * Anzahl, 2)
    # Verfügbarmachen des Wertes für die Grundfläche aus dem lokalen Kontext in den globalen
    return pizzaflaeche

# Berechnung des Preises pro Quadratzentimeter basierend auf dem Preis und der Pizzafläche
def quadratzentimeter_berechnung(Preis, Pizzaflaeche):
    # Zuweisen des Ergebnisses zur lokalen Variable preisproqz
    preisproqz = round(Preis / (Pizzaflaeche), 5)
    # Verfügbarmachen des Wertes für die Grundfläche aus dem lokalen Kontext in den globalen
    return preisproqz

# Setzen einer Variable zum Umsetzen der Abbruchmethode der while-Schleife
ungueltige_eingabe = True

# Ausführen der while-Schleife für die Abfrage der Anzahl, des Durchmessers sowie Preises
while ungueltige_eingabe:
    # Technische Prüfung, ob der User auch wirklich int/float eingegeben hat
    try:
        # Abfragen von Anzahl, Durchmesser, Preis und zuweisen zu gleichnamigen globalen Variablen
        anzahl = int(input("Wie viele Pizzen sollen berechnet werden: "))
        radius = float(input("Welchen Radius hat eine Pizza in cm: "))
        preis = float(input(("Wie viel kostet das Angebot insgesamt: ")))
        ungueltige_eingabe = False
    # Abfangen des Fehlers und Ausgabe eines Fehlerhinweises
    except:
        print("Bitte geben Sie für die Anzahl nur ganze Zahlen und für Durchmesser und Preis nur Kommazahlen ein.")

# Mehrfachausgabe mit Aufruf der Funktion pizzaumfang() mitsamt des Radius und Ausgabe des Ergebnisses
print("Ihr Kreisumfang der Pizza beträgt:", pizzaumfang(radius), "Zentimeter.")
# Mehrfachausgabe mit Aufruf der Funktion pizzaflaeche() mitsamt des Radius und der Anzahl und Ausgabe des Ergebnisses
print("Die Fläche der Pizza beträgt", pizzaflaeche(radius, anzahl), "Quadratzentimeter.")
# Mehrfachausgabe mit Aufruf der Funktion quadratzentimeter_berechnung() mitsamt des Preises
# und dem Ergebnis der Funktion pizzaflaeche() mit den Parametern für die Größe und Anzahl
print("Ein Quadratzentimeter Pizza kostet", quadratzentimeter_berechnung(preis, pizzaflaeche(radius, anzahl)), "€.")