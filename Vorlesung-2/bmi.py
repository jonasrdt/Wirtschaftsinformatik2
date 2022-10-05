# Entwickeln Sie ein Programm, mithilfe dessen der BMI einer
# Person berechnet werden kann
# Hierbei gilt: m ist die Körpermasse in Kilogramm
#               l ist die Körpergröße in Metern

# Definition der benötigten Variablen
koerpergroesse_in_metern = float(input("Bitte geben Sie Ihre Größe in Metern an: "))
koerpergewicht_in_kilogramm = float(input("Bitte geben Sie Ihr Gewicht in Kilogramm an: "))

# Berechnung des Body-Mass-Indexes
bmi = round(koerpergewicht_in_kilogramm / (koerpergroesse_in_metern**2), 2)

# Ausgabe des berechneten Wertes
print("Bei einem Gewicht von:", koerpergewicht_in_kilogramm, "kg und einer Größe von:", koerpergroesse_in_metern, "Metern, beträgt der BMI:", bmi)