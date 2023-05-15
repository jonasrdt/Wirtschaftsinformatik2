# Aufgabe 2 Erweitern Sie die Aufgabe 1 und bringen Sie die Berechnung des Body-Mass-Index (BMI) 
# in eine Funktion.

# Code aus Aufgabe 2 kopiert

def bmi_berechnung(gewicht,groeße):
    """
    The function calculates the body mass index (BMI) based on weight and height inputs.
    
    :param gewicht: weight in kilograms
    :param groe: I believe there is a typo in your question. I assume you meant to write "groeße"
    instead of "groe:"
    """
    bmi = round(gewicht/(groeße**2),1)
    return bmi
    

def bmi_interpretation(bmi):
    """
    The function takes a BMI value as input and returns a corresponding interpretation of the BMI
    category.
    
    :param bmi: The parameter "bmi" is a numeric value representing the Body Mass Index (BMI) of a
    person. The BMI is calculated by dividing a person's weight in kilograms by the square of their
    height in meters. It is commonly used as an indicator of whether a person has a healthy weight or
    not
    """
    if bmi < 18.5:
         bmi_interpretation = "Untergewicht"
    elif 18.5 <= bmi <= 24.9: 
        bmi_interpretation = "Normalgewicht"
    elif 25.0 <= bmi <= 29.9: 
        bmi_interpretation = "Übergewicht"
    else: 
        bmi_interpretation = "starkes Übergewicht"
    return bmi_interpretation



korrekte_groeße = False
korrektes_gewicht = False

while not korrekte_groeße:
    try:  
        groeße = float(input("Bitte geben Sie Ihre Größe in Metern ein: "))
        if 1.45 <= groeße <= 2.10:
                    korrekte_groeße = True
        else:
            print("Bitte geben Sie nur eine realistische Größe in Metern ein!")
    except:
        print("Bitte geben Sie nur eine realistische Größe in Metern ein!")


while not korrektes_gewicht:
    try:  
        gewicht = float(input("Bitte geben Sie Ihr Gewicht in Kg ein: "))
        if 45 <= gewicht <= 150:
            korrektes_gewicht = True
        else:
            print("Bitte geben Sie nur ein realistisches Gewicht ein!")
    except:
        print("Bitte geben Sie nur ein realistisches Gewicht ein!")


# Definieren der Variable bmi, da diese mehrfach genutzt werden soll
bmi = bmi_berechnung(gewicht, groeße)

print("Ihr berechneter BMI beträgt:", bmi,". Interpretiert bedeutet dies, dass Sie", bmi_interpretation(bmi), "haben.")