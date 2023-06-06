# Ergänzen Sie die nachstehende Funktion mithilfe einer Schleife so,
# dass die Keys (Namen) des Dictionaries `telefonbuch` untereinander ausgegeben werden.

def phonebook(telefonbuch):
    # Ergänzen Sie hier Ihre Lösung
    for key in telefonbuch:
        print(key, "hat die Telefonnummer", telefonbuch[key])

#                  key       value
telefonbuch = {"Christian": 2105070,
                "Jonas": 2105071,
                "Miriam": 2105072}

phonebook(telefonbuch)