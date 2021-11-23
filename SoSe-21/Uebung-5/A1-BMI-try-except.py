# Aufgabe 1 - Übung 5
#
# Erweitern Sie das BMI-Programm aus der Vorlesung und geben Sie zusätzlich die folgende Interpretation aus:
# BMI < 18.5 Untergewicht
# BMI 18.5 - 24.9 Normalgewicht
# BMI 25.0 - 29.9 Übergewicht
# BMI > 30.0 Adipositas
#
# BMI = masse / (körpergröße zum quadrat in m)

untergewicht = 18.5
normalgewichtTop = 24.9
normalgewichtBottom = 18.5
uebergewichtTop = 29.9

uebergewichtBottom = 25
adipositas = 30

# Abfrage einer Nuterzeingabe für die Größe einer Person
groesse_input = False
while not groesse_input:
    try:
        groesse = float(input("Bitte geben Sie Ihre Größe in cm ein:"))
        print ("Die von Ihnen eingegebene Größe ist:", groesse)
        groesse_input = True
    except:
        print("Bitte geben Sie nur Zahlen ein.")

# Abfrage einer Nuterzeingabe für das Gewicht einer Person
gewicht_input = False
while not gewicht_input:
    try:
        gewicht = float(input("Bitte geben Sie Ihr Gewicht in kg ein:"))
        print ("Das von Ihnen eingegebene Gewicht:", gewicht)
        gewicht_input = True
    except:
        print("Bitte geben Sie nur Zahlen ein.")


# Berechnung des BMI
def bmi(groesse, gewicht):
    werte_berechnung = round(gewicht/((groesse/100)**2), 1)
    return werte_berechnung

berechneter_BMI = bmi(groesse,gewicht)
print ("Mit einer Größe von", groesse, "und einem Gewicht von", gewicht, "beträgt Ihr BMI", berechneter_BMI)

# Bewertung des BMI
if berechneter_BMI < untergewicht:
    print ("Der BMI fällt in den Bereich des Untergewichts.")
elif normalgewichtBottom < berechneter_BMI < normalgewichtTop:
    print ("Der BMI liegt im Normalbereich.")
elif uebergewichtBottom < berechneter_BMI < uebergewichtTop:
    print ("Der BMI liegt im übergewichtigen Bereich.")
elif berechneter_BMI > adipositas:
    print ("Der BMI liegt im Bereich Adipositas.")
else:
    print("Der BMI konnte nicht zugeordnet werden.")