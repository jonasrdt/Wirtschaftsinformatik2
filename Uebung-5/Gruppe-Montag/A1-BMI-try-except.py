# Aufgabe 1 - Übung 5
# 
# Berechnung des Body-Mass-Index
# bmi = körpermasse (in kg) / körpergröße zum quadrat
# Ergebnis: Maßeinheit in kg/m^2

# Variablendefinition
# float = Fließkommazahlen
# int = Ganze Zahlen
# str = String => Zeichenketten
# bool = True or False

# Die while-Schleife läuft solange durch, bis es eine gültige Eingabe gibt
gueltige_groesse = False
while not gueltige_groesse:
    try:
        groesse = float(input("Bitte geben Sie Ihre Größe in cm ein: "))
        # Die Größe muss größer oder gleich 50 sein und gleichzeitig kleiner oder gleich 280 sein
        if 50 <= groesse <= 280:
            print ("Die von Ihnen eingegeben Größe lautet:", groesse)
            gueltige_groesse = True
        else:
            print("Bitte geben Sie eine realistische Größe ein.")
    except:
        print("Bitte geben Sie nur Zahlen ein.")

gueltiges_gewicht = False
while not gueltiges_gewicht:
    try:
        gewicht = float(input("Bitte geben Sie Ihr Gewicht in kg ein: "))
        if 30 <= gewicht <= 500:
            print ("Das von Ihnen eingegeben Gewicht beträgt in kg:", gewicht)
            gueltiges_gewicht = True
        else:
            print("Bitte geben Sie ein realistisches Gewicht ein.")
    except:
        print("Bitte geben Sie nur Zahlen ein.")

# Berechnung des BMI und runden auf 2 Nachkommastellen
def bmi(gewicht, groesse):
    return round((gewicht/(groesse/100)**2),2)

print ("Bei einer Größe von:", groesse, "cm und einem Gewicht von:", gewicht, "kg beträgt Ihr BMI:", bmi(gewicht,groesse))
