
tante_emma_laden = {
                    "Brot": 5,
                    "Käse": 10,
                    "Senf": 2.50
                    }

for element in tante_emma_laden.keys():
    print("Im Tante Emma laden befindet sich:", element)

# Ergänzen Sie das Programm so, dass der Nutzer eine Ware eingibt und
# daraufhin der Preis pro Stück ausgegeben
ware = input("Bitte geben Sie die Ware ein: ")
print("Ein",ware,"kostet:", tante_emma_laden[ware], "€.")


# Ergänzen Sie das Programm so, dass der Nutzer eine Ware eingibt,
# geprüft wird, ob sich die Ware Bestand befindet und wenn ja
# daraufhin der Preis pro Stück ausgegeben
ware_im_bestand = False
while not ware_im_bestand:
    ware = input("Bitte geben Sie die Ware ein: ")
    if ware in tante_emma_laden:
        print("Ein",ware,"kostet:", tante_emma_laden[ware], "€.")
        ware_im_bestand = True
    else:
        print("Die Ware", ware, "befindet sich nicht im Bestand. Bitte geben Sie etwas anderes ein.")