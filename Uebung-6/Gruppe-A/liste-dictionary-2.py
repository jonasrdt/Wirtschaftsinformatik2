

# Kann mehrere Werte von mehreren Datentypen speichern
# und ist ein so genannter Key-Value-Storage
#               Key        Value
telefonbuch = {"Jonas": "01239812354",
              "Annika": "01239812354",
              "Fabian": "01239812354",
              "Nadine": "01239812354",
              "Tamara": "01239812354",
              "Tim": "01239812354",
              "Jesper": "01239812354",
              "Jannis": "01239812354"}

# The above code is asking the user to input a name and then it checks if the name is in the
# dictionary. If the name is in the dictionary, it prints the name and the corresponding phone number.
# If the name is not in the dictionary, it asks the user if they want to add the name and phone number
# to the dictionary. If the user says yes, it asks the user to input the phone number and then adds
# the name and phone number to the dictionary.
name = input("Bitte geben Sie den Namen ein, dessen Telefonnummer Sie erfahren wollen: ")
if name in telefonbuch:
    print("Die Telefonnummer von", name, "lautet:", telefonbuch[name])
else:
    print("Der Name", name, "ist nicht im Telefonbuch vorhanden.")
    entscheidung = input("Wollen Sie hierfür eine Telefonnummer hinterlegen (ja/nein): ")
    if entscheidung.lower() == "ja":
        telefonnummer = input("Bitte geben Sie die Telefonnummer ein: ")
        telefonbuch.update({name: telefonnummer})
        print(name, "wurde dem Telefonbuch hinzugefügt.")
        print(telefonbuch)