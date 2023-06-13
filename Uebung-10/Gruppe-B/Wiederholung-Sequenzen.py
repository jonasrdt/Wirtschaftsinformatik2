# Index 01234
name = "Jonas"   # Datentyp String (str) => Zeichenkette (auch Sequenz genannt)

# Gib die Zeichen von Beginn bis zum Index 2 aus
print(name[:2])

# Gib die Zeichen vom Ende bis zum Index 2 aus
print(name[2:])


einkaufsliste = [12, 'Kirschen',    # Datentypen Liste (list) => Kann alle möglichen Datentypen enhalten
                 10, 'Erdbeeren',
                 5, 'Äpfel',]


# The code is iterating over each element in the list `einkaufsliste` and printing each element on a
# new line. The variable `eintrag` is used to represent each element in the list during each iteration
# of the loop.
for eintrag in einkaufsliste:
    print(eintrag)
    
#               Key           Value
telefonbuch = {"Jonas":     "017394321",    # Datentyp Dictionary (dict) => Key, Value Store der auch alle möglichen Datentypen enthalten kann
               "Christian": "01892393"}

# The code is iterating over each key in the dictionary `telefonbuch` and printing each key on a new
# line. The variable `key` is used to represent each key in the dictionary during each iteration of
# the loop.
for peter in telefonbuch:
    print(peter)