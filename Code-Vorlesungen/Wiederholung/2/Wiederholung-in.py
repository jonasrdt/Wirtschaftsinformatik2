
warenlager = {"Schrauben": 500,
              "Nieten": 150,
              "2m Stahlträger": 250
              }

print(warenlager)
warenlager.update({"Muttern": 50}) # Hinzufügen eines neuen Elements zum Dictionary
print(warenlager)
warenlager.update({"Schrauben": 310}) # Ändern der Anzahl eines Elements
print(warenlager)
warenlager.pop("Schrauben") # Löschen eines Elements
print(warenlager)
warenlager.clear() # Löschen des gesamten Dictionaries
print(warenlager)

abfrage = input("Von welchem Posten wollen Sie die verfügbare Anzahl im Lager wissen: ")

if abfrage in warenlager:
    print("Die Menge beträgt:", warenlager[abfrage])


beliebiger_string = "Hier steht Text über Jonas"

if "Jonas" in beliebiger_string:
    print("Hurra")