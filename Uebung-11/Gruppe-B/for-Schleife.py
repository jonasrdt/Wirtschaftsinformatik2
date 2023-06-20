
# Bei einer for-Schleife kennen wir
# die Anzahl der Schleifendurchläufe.

# range(1,15) läuft BIS 15, nicht einschl. 15
# Ausgabe also: 1....14
# range(start, stop, step) wenn kein step gegeben, step steigt um 1
for zaehler in range(1,15):
    print(zaehler)

# Start: 1, Ende: 15, Step: 2
for zaehler_2 in range(1,15, 2):
    print(zaehler)

# Rückwärts zählen mit for-Schleife
# Start: 15, Ende: 1, Step: -1
for zaehler_3 in range(15, 1, -1):
    print(zaehler_3)
    
# range(15) läuft also 15-Mal durch
# beginnt jedoch bei 0
for i in range(15):
    print(i)

