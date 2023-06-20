

# Iterierbare Objekte, welche mit dem Membership-Operator
# 'in' und einer for-Schleife ausgegeben werden können

name = "Jonas"
# Gibt jeden Buchstaben des Strings aus
for buchstabe in name:
    print(buchstabe)

studierende = ["Lisa", "Peter", "Hans"]
# Gibt jedes Element der Liste aus
for member in studierende:
    print(member)

#               Key         Value
telefonbuch = {"Jonas": "0431129456",
               "Christian": "04346546789"}
# Gibt die einzelnen Keys innerhalb des Dictionaries aus
for eintrag in telefonbuch.keys():
    print(eintrag)
# Gibt die einzelnen Values innerhalb des Dictionaries aus
for telefonnummer in telefonbuch.values():
    print(telefonnummer)
