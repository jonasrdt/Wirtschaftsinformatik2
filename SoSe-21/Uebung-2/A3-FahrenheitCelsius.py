# Aufgabe 3 - Übung 2
# 
# Erstellen Sie ein Python-Programm mit den folgenden Anforderungen:
#   - Umrechnung von Fahrenheit nach Celsius
#   - Umrechnung von Celsius nach Fahrenheit
# Dies kann sicher helfen: Celsius = 5/9 * (Fahrenheit - 32).


# 1. Nutzereingabe für Celsius erfassen und in float umwandeln
celsiusInput = float(input("Bitte geben Sie einen Celsius Wert ein:"))
print("Ihre Eingabe für Celsius betrug:", celsiusInput)

# 2. Umrechnung von Celsius in Fahrenheit und Runden auf zwei Nachkommastellen
fahrenheitCalculated = round((celsiusInput * (9/5) + 32),2)
print (celsiusInput, "Celsius sind umgerechnet", fahrenheitCalculated, "Fahrenheit.")

# 3. Nutzereingabe für Fahrenheit erfassen und in float umwandeln
fahrenheitInput = float(input("Bitte geben Sie einen Fahrenheit Wert ein:"))
print("Ihre Eingabe für Fahrenheit betrug:", fahrenheitInput)

# 4. Umrechnung von Fahrenheit in Celsius und Runden auf zwei Nachkommastellen
celsiusCalculated = round((5/9) * (fahrenheitInput - 32),2)
print (fahrenheitInput, "Fahrenheit sind umgerechnet", celsiusCalculated, "Celsius.")