# Mithilfe von if-elif-else können wir das
# Verhalten des Programmes, bspw. auf Basis von Eingabe
# des Users, steuern.

zahl_1 = 5
zahl_2 = 12

# Prüfung, ob die mit dem if-Statement verknüpfte Bedingung WAHR (True) ist
if zahl_1 > zahl_2:
    print("Mathe ist kaputt.")
# Andernfalls wird das else-Statement ausgeführt
else:
    print("Juhu. Mathe funktioniert.")

# Eingabe durch den Nutzer, um diese Eingabe anschließend
# innerhalb des if-elif-else-Statements zu prüfen
nutzereingabe = input("Bitte geben Sie Ihren Namen ein: ")

# .lower() damit wir eindeutig vergleichen können.
# Prüfen, ob und welche der Eingaben zutrifft und entsprechende
# Ausgabe mithilfe von print(). Durch die Nutzung von elif
# wird die gesamte Abfrage miteinander verknüpft.
if nutzereingabe.lower() == 'jonas':
    print("Hallo Jonas.")
elif nutzereingabe.lower() == 'jastin':
    print("Hallo Jastin.")
else:
    print("Ich glaube wir kennen uns noch nicht.")