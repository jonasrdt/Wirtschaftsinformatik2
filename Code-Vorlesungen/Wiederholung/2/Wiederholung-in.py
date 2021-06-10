
warenlager = {"Schrauben": 500,
              "Nieten": 150,
              "2m Stahlträger": 250
              }

print(warenlager)
warenlager.update({"Muttern": 50})
print(warenlager)
warenlager.update({"Schrauben": 310})
print(warenlager)
warenlager.pop("Schrauben")
print(warenlager)
warenlager.clear()
print(warenlager)

abfrage = input("Von welchem Posten wollen Sie die verfügbare Anzahl im Lager wissen: ")

if abfrage in warenlager:
    print("Die Menge beträgt:", warenlager[abfrage])


beliebiger_string = "Hier steht Text über Jonas"

if "Jonas" in beliebiger_string:
    print("Hurra")