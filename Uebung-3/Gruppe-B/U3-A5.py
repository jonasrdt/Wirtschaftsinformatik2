
# Variablendefinition
hoechststeuersatz = 0.26
mittlerersteuersatz = 0.22
niedrigersteuersatz = 0.18

# Eingabe des Bruttogehalts und Ändern des Datentyps von string auf float
bruttogehalt = float(input("Bitte geben Sie Ihr Bruttogehalt ein: "))
print("Sie haben ein Bruttogehalt i.H.v.", bruttogehalt, "€ eingegeben.")

# Eingabe des Familienstands
familienstand = input("Bitte geben Sie Ihren Familienstand an (ledig/verheiratet): ")
print("Sie haben den Familienstand", familienstand, "angegeben.")

if bruttogehalt > 4000 and familienstand.lower() == "ledig":
    steuern = bruttogehalt * hoechststeuersatz
    print("Auf Ihr Gehalt i.H.v.", bruttogehalt, "€ fallen", steuern,"€ Steuern an.")
    
elif bruttogehalt > 4000 and familienstand.lower() == "verheiratet":
    steuern = bruttogehalt * mittlerersteuersatz
    print("Auf Ihr Gehalt i.H.v.", bruttogehalt, "€ fallen", steuern,"€ Steuern an.")
    
elif 0 < bruttogehalt <= 4000 and familienstand.lower() == "ledig":
    steuern = bruttogehalt * mittlerersteuersatz
    print("Auf Ihr Gehalt i.H.v.", bruttogehalt, "€ fallen", steuern,"€ Steuern an.")
    
elif 0 < bruttogehalt <= 4000 and familienstand.lower() == "verheiratet":
    steuern = bruttogehalt * niedrigersteuersatz
    print("Auf Ihr Gehalt i.H.v.", bruttogehalt, "€ fallen", steuern,"€ Steuern an.")

else:
    print("Sie haben vermutlich ein negatives Bruttogehalt eingegbeen. Das ist Quatsch.")