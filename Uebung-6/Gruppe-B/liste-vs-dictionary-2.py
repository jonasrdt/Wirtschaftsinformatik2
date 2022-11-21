
#               Key       Value
telefonbuch = {"Miray": "9013823",
               "Nicolas": "9083172",
               "Jaqueline": "98078631",
               "Bennett": "21839844",
               "Jonas": "3123891"}

telefonbuch.update({"Nicolas": "8973490234"})
telefonbuch.update({"Hans Peter": "3124545345"})

# Asking the user to input a name and then it checks if the name is in the dictionary. If it is, it
# prints the name and the number. If it is not, it asks the user if they want to add the name and
# number to the dictionary. If they say yes, it asks for the number and then adds it to the
# dictionary.
name = input("Bitte geben Sie den Namen ein, dessen Telefonnummer Sie erfahren wollen: ")
if name in telefonbuch:
    print("Die Telefonnummer von", name, "lautet:", telefonbuch[name])
else:
    print("Zu dem Namen konnte kein Eintrag gefunden werden.")
    entscheidung = input("Möchten Sie den Eintrag hinzufügen (ja/nein): ")
    if entscheidung.lower() == "ja":
        telefonnummer = input("Bitte geben Sie die zugehörige Telefonnummer ein: ")
        telefonbuch.update({name: telefonnummer})
        print(name, "wurde erfolgreich hinzugefügt:", telefonbuch)