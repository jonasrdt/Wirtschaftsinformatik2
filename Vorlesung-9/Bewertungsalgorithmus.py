# Schreiben Sie ein Programm, welches auf Basis einer zufälligen
# Zahl entscheidet welcher Student / welche Studentin die Klausur
# besteht und welche/r nicht.

bestanden = []
nicht_bestanden = []

#                   0           1         2         3         4       5
studierende = ['Alexandra', 'Zülfiye', 'Mariam', 'Parisa', 'Alex', 'Gavin']
print("Auf der Liste befinden sich", len(studierende), "Studierende.")

for zaehler in range(0, len(studierende)):
    if ((zaehler % 2) != 0) and (zaehler != 0):
        bestanden.append(studierende[zaehler])
    else:
        nicht_bestanden.append(studierende[zaehler])

print("Bestanden haben:", bestanden)
print("Nicht bestanden haben:", nicht_bestanden)