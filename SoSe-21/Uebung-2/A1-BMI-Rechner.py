# Aufgabe 1 - Übung 2
# 
# Berechnung des Body-Mass-Index
# bmi = körpermasse (in kg) / körpergröße zum quadrat
# Ergebnis: Maßeinheit in kg/m^2

# Variablendefinition
# float = Fließkommazahlen
# int = Ganze Zahlen
# str = String => Zeichenketten

groesse = float (input("Bitte geben Sie Ihre Größe in cm ein:"))
print ("Die von Ihnen eingegeben Größe lautet:", groesse)

gewicht = float(input("Bitte geben Sie Ihr Gewicht in kg ein:"))
print ("Das von Ihnen eingegeben Gewicht beträgt in kg:", gewicht)

# Berechnung des BMI und runden auf 2 Nachkommastellen
bmi = round((gewicht/(groesse/100)**2),2)
print ("Bei einer Größe von:", groesse, "cm und einem Gewicht von:", gewicht, "kg beträgt Ihr BMI:", bmi)