# Aufgabe 2 - Übung 3
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
groesse = float(input("Bitte geben Sie Ihre Größe in cm ein:"))
print ("Die von Ihnen eingegebene Größe ist:", groesse)

# Abfrage einer Nuterzeingabe für das Gewicht einer Person
gewicht = float(input("Bitte geben Sie Ihr Gewicht in kg ein:"))
print ("Das von Ihnen eingegebene Gewicht:", gewicht)

# Berechnung des BMI
bmi = round(gewicht/((groesse/100)**2), 1)
print (groesse, "Ihr berechneter BMI beträgt: ", bmi,)

# Bewertung des BMI
if bmi < untergewicht:
    print ("Der BMI fällt in den Bereich des Untergewichts.")
elif normalgewichtBottom < bmi < normalgewichtTop:
    print ("Der BMI liegt im Normalbereich.")
elif uebergewichtBottom < bmi < uebergewichtTop:
    print ("Der BMI liegt im übergewichtigen Bereich.")
elif bmi > adipositas:
    print ("Der BMI liegt im Bereich Adipositas.")
else:
    print("Der BMI konnte nicht zugeordnet werden.")