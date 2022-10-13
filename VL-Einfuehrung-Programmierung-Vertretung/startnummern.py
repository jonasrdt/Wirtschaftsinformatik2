import random
random.seed()

# Initialisieren der Liste
startnummern = []

# Abfragen der Anzahl der Nummern
anzahl_startnummern = int(input("Bitte geben Sie Anzahl der auszugebenen Startnummern an: "))

for startnummer in range (1, anzahl_startnummern+1):
    random_startnummer = random.randint(1,anzahl_startnummern)
    startnummern.append(random_startnummer)

print("Es wurden", len(startnummern), "Startnummern erstellt.")
print(startnummern)
