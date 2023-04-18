

koerpergroesse_in_m = float(input("Bitte geben Sie Ihre Körpergröße in Metern an: "))
gewicht_in_kg = float(input("Bitte geben Sie Ihr Gewicht in Kilogramm an: "))

bmi = round(gewicht_in_kg / (koerpergroesse_in_m**2), 1)

print("Ihr BMI beträgt:", bmi)

if bmi <= 18.5 :
    print("Ihr BMI beträgt", bmi, "gemäß Tabelle entspräche das einem Untergewicht.")
elif 18.5 <= bmi <= 24.9:
    print("Ihr BMI beträgt", bmi, "gemäß Tabelle entspräche das dem Normalgewicht.")
elif 25 <= bmi <= 29.9:
    print("Ihr BMI beträgt", bmi, "gemäß Tabelle entspräche das dem Überwicht.")
elif bmi >= 30:
    print("Ihr BMI beträgt", bmi, "gemäß Tabelle entspräche das dem Adipositas.")
else:
    print("Der berechnete Wert kann nicht in die Tabelle eingeordnet werden.")
