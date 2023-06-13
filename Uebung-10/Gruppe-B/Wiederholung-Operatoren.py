
zahl_1  = 5
zahl_2 = 12

# Klassische Operatoren
divison = zahl_1 / zahl_2
multiplikation = zahl_1 * zahl_2
addieren = zahl_1 + zahl_2
subtrahieren = zahl_1 - zahl_2
potenzieren = zahl_1 ** 2 # Mit Exponent '2'
potenzieren = zahl_1 ** 3 # Mit Exponent '3'

# Vergleichsoperatoren => Ergebnis immer Boolean (bool)
print(zahl_1 > zahl_2)  # Größer als … => False
print(zahl_1 < zahl_2)  # Kleiner als … => True
print(zahl_1 <= zahl_2) # Kleiner gleich als … => False
print(zahl_1 >= zahl_2) # Größer gleich als … => False
print(zahl_1 == zahl_2) # Absolute Gleichheit => False

# Modulo % => Teilen mit Rest
print(zahl_2 % zahl_1) # 12 / 5 => Rest 2

# Beispiel für Prüfung, ob Anzahl Elemente in einer Liste gerade oder ungerade ist
liste = [1, 2, 3, 4, 5]
if (len(liste) % 2) == 0:
    print("Die Anzahl der Elemente ist gerade.")
else:
    print("Die Anzahl der Elemente ist ungerade.") 
