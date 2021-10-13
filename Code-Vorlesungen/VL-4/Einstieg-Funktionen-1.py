

# Funktion definieren, die Sternchen in die Konsole ausgibt
def sternchenausgabe(anzahl_sternchen):
    for i in range(anzahl_sternchen):
        print("Brötchen", end=" ")
    print()

print("Hier kommen die Sternchen:")
# Ausführen der Funktion
sternchenausgabe(5)
print("Hier kommen noch mehr:")
# Ausführen der Funktion
sternchenausgabe(10)
