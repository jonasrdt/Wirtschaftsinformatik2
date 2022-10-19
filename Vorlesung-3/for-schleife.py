# for-Schleife nutzen wir dann, wenn wir der Anzahl der Durchläufe kennen
# for zaehler in range(start, stop, step)

# Lammgulasch mit Ras el Hanout
# mit beliebiger Anzahl an Knoblauchzehen

gesamtzahl_knoblauchzehen = int(input("Wie viele Knoblauchzehen sollen geschnitten werden: "))

for knoblauchzehe in range(1, gesamtzahl_knoblauchzehen + 1):
    print("Ich schneide Knoblauchzehe Nr.", knoblauchzehe)
    print("Hmmm....das riecht aber lecker.")
print("Ich habe fertig.")