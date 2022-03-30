# Variablendefinition
kontostand = 5000

# Ausgabe des aktuellen Kontostands
print("Ihr Kontostand beträgt aktuell: ", kontostand, "€.")
# Nutzereingabe für die Höhe des Überweisungsbetrags
ueberweisung = float(input("Bitte geben Sie den Überweisungsbetrag ein: "))
print("Sie haben", ueberweisung,"€ eingegeben.")

# Kontrollstruktur, um zu prüfen, ob der Kontostand ausreicht, um die Überweisung zu tätigen
if(ueberweisung <= kontostand):
    print("Die Überweisung i.H.v.", ueberweisung, "€ wurde getätigt.")
    # Ausgabe des neuen Kontostands
    print("Ihr neuer Kontostand beträgt", kontostand - ueberweisung, "€.")
else:
    print("Ihr Kontostand i.H.v.", kontostand,"reicht nicht aus, um", ueberweisung, "€ zu überweisen.")