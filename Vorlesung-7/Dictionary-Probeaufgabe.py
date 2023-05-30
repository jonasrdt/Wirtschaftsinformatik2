# Schreiben Sie handschriftlich ein Python-Programm,
# mithilfe dessen bei Nutzereingabe eines Namens die passende
# Telefonnummer aus dem Adressbuch mitsamt des Namens ausgegeben wird. Falls der Name
# im Dictionary nicht existiert,
# soll ein neuer Eintrag mit einer neuen Telefonnummer eingetragen werden. Nehmen Sie
# folgendes Dictionary als Basis:

adressbuch = {
    "Lara" : "05761496961",
    "Jan" : "0611135160"
}

name = input("Bitte geben Sie einen Namen ein: ")
if name in adressbuch:
    print("Die Telefonnummer von", name, "lautet:", adressbuch[name])
else:
    print("Der Name kommt nicht in dem Dictionary vor.")
    nummer = int(input("Bitte geben Sie die Telefonnummer der Person ein: "))
    # Hinzufügen der Variable 'name' als key und der Variable 'nummer' als value
    adressbuch.update({name: nummer})
    print(name, "wurde mit der Nummer", nummer, "zum Adressbuch hinzugefügt.")
