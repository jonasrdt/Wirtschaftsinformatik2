# for-Schleife hat eine festgelegte Anzahl an Durchläufen

# Zähler => Stunden
# Range => 1 bis 6, also alles BIS 6 und EINSCHLIESSLICH 5
# range(start, stop, step)
for stunden in range(1,6):
    print("Du arbeitest seit", stunden, "Stunden.")


# Variablendefinition
anzahl_zwiebeln = 4

# Zähler => zwiebel
# Range 1 bis anzahl_zwiebeln + 1, damit alle Zwiebeln geschnitten werden
for zwiebel in range(1,anzahl_zwiebeln + 1):
    print("Ich schneide Zwiebel Nummer", zwiebel)
    print("… und muss furchtbar doll weinen.")
    
# Ausgeben, wenn die Schleife durchgelaufen ist
print("---------------------------------------")
print("Ich habe insgesamt", anzahl_zwiebeln,"Zwiebeln geschnitten.")