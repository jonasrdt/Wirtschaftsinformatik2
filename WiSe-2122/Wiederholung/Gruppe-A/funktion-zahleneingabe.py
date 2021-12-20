def zahleneingabe(text):
    falsche_eingabe = True
    while falsche_eingabe:
        try:
            zahl = int(input(text))
            falsche_eingabe = False
        except:
            print("Bitte geben Sie nur ganze Zahlen ein.")
    return zahl


alter = zahleneingabe("Bitte geben Sie Ihr Alter ein: ")
print("Alter ist:", alter)

gewicht = zahleneingabe("Bitte geben Sie Ihr Gewicht als Ganzzahl ein: ")
print("Gewicht ist:", gewicht)

menge = zahleneingabe("Bitte geben Sie die Menge ein: ")
print("Menge ist:", menge)