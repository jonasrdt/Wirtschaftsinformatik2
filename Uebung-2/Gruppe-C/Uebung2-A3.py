# Erstellen Sie ein Python-Programm mit den folgenden Anforderungen:
# Umrechnung von Fahrenheit nach Celsius
# Umrechnung von Celsius nach Fahrenheit
# Dies kann sicher helfen:
# Celsius = 5/9 * (Fahrenheit - 32).

# Umrechnung von Fahrenheit in Celsius mit Rundung auf zwei Nachkommastellen
fahrenheit = round(float(input("Bitte geben Sie eine Temperatur in Fahrenheit ein: ")),2)
celsius = round(5/9 * (fahrenheit - 32), 2)
print(fahrenheit, "Grad Fahrenheit =", celsius, "Grad Celsius.")

# Umrechnung von Celsius in Fahrenheit mit Rundung auf zwei Nachkommastellen
celsius = round(float(input("Bitte geben Sie eine Temperatur in Celsius ein: ")))
fahrenheit = (celsius * 1.8) + 32
print(celsius, "Grad Celsius =", fahrenheit, "Grad Fahrenheit.")
