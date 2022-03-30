# Erstellen Sie ein Python-Programm mit den folgenden Anforderungen:
# • Umrechnung von Fahrenheit nach Celsius
# • Umrechnung von Celsius nach Fahrenheit
# Dies kann sicher helfen:
# Celsius = 5/9 * (Fahrenheit - 32).


# Umrechnung von Fahrenheit nach Celsius mit Runden auf eine Nachkommastelle
fahrenheit = float(input("Bitte geben Sie eine Temperatur in Fahrenheit ein: "))
celsius = round(5/9 * (fahrenheit - 32), 1)
print(fahrenheit, "Grad Fahrenheit ergeben", celsius, "Grad Celsius.")

# Umrechnung von Celsius nach Fahrenheit mit Runden auf eine Nachkommastelle
celsius = float(input("Bitte geben Sie eine Temperatur in Celsius ein: "))
fahrenheit = round((celsius / (5/9)) + 32, 1)
print(celsius, "Grad Celsius ergeben", fahrenheit, "Grad Fahrenheit.")
