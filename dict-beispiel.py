
# liste = [["Jonas", 123456], ["Christian", 889988], True, "Peter"]

#                 keys     values
kontakte_dict = {"Jonas": 123456,
                "Christian": 889988,
                "Lina": 776644}

kontakte_list = [["Jonas", 123456],
                 ["Christian", 889988],
                 ["Lina", 776644]]

# Telefonnummer von Christian per Dictionary abfragen
print("Die Telefonnummer von Lina lautet:", kontakte_dict["Lina"])
print("Diese Telefonnummern sind vorhanden: ")
print(kontakte_dict.values())
print("Diese Kontaktnamen sind vorhanden: ")
print(kontakte_dict.keys())
print("Diese Kontakte sind vorhanden: ")
print(kontakte_dict.items())

# Telefonnummer von Christian per Liste abfragen
for kontakte in kontakte_list:
    if kontakte[0] == "Lina":
        print("Die Telefonnummer von Lina lautet:", kontakte[1])


