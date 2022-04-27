# Erweitern Sie das Programm um eine Ausnahmebehandlung, falls fehlerhafte Werte über die Tastatur eingegeben werden.
# Erweitern Sie die Aufgabe 1 und bringen Sie die Berechnung des Body-Mass-Index (BMI) in eine Funktion.
# Programm zur Berechnung des BMI
# BMI = m / l^2

# Funktion zur Berechnung des BMI
def bmirechner(gewicht_in_kg, groesse_in_cm):   
    # Berechnung des BMIs und runden auf zwei Nachkommastellen
    bmi = round(gewicht_in_kg / (groesse_in_cm/100)**2,2)
    return bmi

# Setzen einer Abbruchbedingung
richtige_eingabe = False
while not richtige_eingabe:
    try:
        koerpergewicht_in_kg = float(input("Bitte geben Sie Ihr Körpergewicht in kg ein: "))
        groesse_in_cm = float(input("Bitte geben Sie Ihre Körpergröße in Zentimetern ein: "))
        if 35 <= koerpergewicht_in_kg <= 450 and 50 <= groesse_in_cm <= 250:
            richtige_eingabe = True # Abbruchbedingung
        else:
            print("Bitte geben Sie nur realistische Zahlen ein.")
    except:
        print("Bitte geben Sie nur Zahlen ein.")
        
# Ausführen der Funktion bmirechner(koerpergewicht, groesse) mit den
# vom Nutzer eingegebenen Werten
bmi = bmirechner(koerpergewicht_in_kg, groesse_in_cm)

# Ausgabe des BMIs
print("Bei einer Körpergröße von", groesse_in_cm, "Zentimetern und einem Gewicht von", koerpergewicht_in_kg, "Kilogramm beträgt der Body-Mass-Index:", bmi)

