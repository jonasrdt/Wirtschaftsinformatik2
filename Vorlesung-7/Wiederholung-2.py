


einkaufsliste = [["Brot", 5], ["Käse", 10], ["Wasserflaschen", 6]]

# Aufgabe: Schreiben Sie ein Python-Programm, welches folgende Ausgabe erzeugt
# # Auf der Einkaufsliste befinden sich 3 Gegenstände.
# # Brot:           5 Stück
# # Käse:           10 Stück
# # Wasserflaschen: 6 Stück

print("Auf der Einkaufsliste befinden sich", len(einkaufsliste), "Gegenstände.")

for artikel in einkaufsliste:
    print("Von dem Artikel", artikel[0], "benötigt man", artikel[1], "Artikel.")
    