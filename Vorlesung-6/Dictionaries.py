# Key Value Store
diction_MA = {
    # Key      # Value
    'Akademischer Titel': '',
    'Vorname': 'Jonas',
    'Nachname': 'Reinhardt',
    'Raumnr': '1.14',
    'Telefon': '04312101234',
    'Alter': 29,
    'Anstellungsstatus': True,
    'Getätigte Publikationen': ["blablabla", "blablabla"]
}

# Ausgeben des Values für den Key "Vorname"
print(diction_MA["Vorname"])
neuer_name = input("Geben Sie den neuen Namen ein: ")
# Updaten des Values für den Key "Vorname"
diction_MA.update({"Vorname": neuer_name})
print(diction_MA["Vorname"])

# Ausgeben aller Values des Dictionaries
print(diction_MA.values())