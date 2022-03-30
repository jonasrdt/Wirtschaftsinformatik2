# Erstellen Sie ein Python-Programm mit den folgenden Anforderungen:
# • Umrechnung von Fahrenheit nach Celsius
# • Umrechnung von Celsius nach Fahrenheit
# Dies kann sicher helfen:
# Celsius = 5/9 * (Fahrenheit - 32).
# Außerdem soll sich der Nutzer entscheiden können, was er überhaupt
# berechnen möchte.

entscheidung = input("Willst du (F)ahrenheit-Celsius berechnen oder (C)elsius-Fahrenheit: ")

if (entscheidung == "F"):
    # Umrechnung von Fahrenheit nach Celsius mit Runden auf eine Nachkommastelle
    fahrenheit = float(input("Bitte geben Sie eine Temperatur in Fahrenheit ein: "))
    celsius = round(5/9 * (fahrenheit - 32), 1)
    print(fahrenheit, "Grad Fahrenheit ergeben", celsius, "Grad Celsius.")
elif (entscheidung == "C"):
    # Umrechnung von Celsius nach Fahrenheit mit Runden auf eine Nachkommastelle
    celsius = float(input("Bitte geben Sie eine Temperatur in Celsius ein: "))
    fahrenheit = round((celsius / (5/9)) + 32, 1)
    print(celsius, "Grad Celsius ergeben", fahrenheit, "Grad Fahrenheit.")
else:
    print("Ihre Eingabe war leider ungültig.")