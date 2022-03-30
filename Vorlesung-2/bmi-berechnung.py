# Programm zur Berechnung des BMI
# BMI = m / l^2

# Abfragen der Nutzereingabe
kopergewicht_in_kg = float(input("Bitte geben Sie Ihr Körpergewicht in kg ein: "))
groesse_in_cm = float(input("Bitte geben Sie Ihre Körpergröße in Zentimetern ein: "))

# Berechnung des BMIs und runden auf zwei Nachkommastellen
bmi = round(kopergewicht_in_kg / (groesse_in_cm/100)**2,2)

# Ausgabe des BMIs
print("Bei einer Körpergröße von", groesse_in_cm, "Zentimetern und einem Gewicht von", kopergewicht_in_kg, "Kilogramm beträgt der Body-Mass-Index:", bmi)

