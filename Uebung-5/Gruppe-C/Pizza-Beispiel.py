# Berechnen der Grundfläche einer Pizza

# Variablendefinition
pi = 3.1415

# Erfassen des User-Inputs
durchmesser = int(input("Bitte geben Sie den Durchmesser in CM der Pizza an: "))
radius = durchmesser / 2

# Berechnen der Grundfläche
grundflaeche = pi * (radius**2)
print("Die Grundfläche der Pizza beträgt:", grundflaeche, "Quadratzentimeter.")