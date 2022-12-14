

# for-Schleife, wird solange ausgeführt, wie wir es vorgeben
for zaehler in range(1,11):
    print("Durchlauf Nr.:", zaehler)

# Eindimensionale Liste
einkaufsliste = ['Wildfond', 'Keule vom Rehwild', 'Lorbeer', 'Rotwein']

# Iterieren durch Listen und Ausgeben jedes einzelnen Listenelements
for element in einkaufsliste:
    print("Auf der Einkaufsliste steht:", element)

# Verschachtelte for-Schleife: Die innere Schleife läuft immer komplett durch
# die äußere Schleife zählt jedes Mal, nachdem die innere einmal komplett durchgelaufen ist
# einen hoch
for zeilen in range(5):
    for spalten in range(10):
        print("*", end= " ")
    print()