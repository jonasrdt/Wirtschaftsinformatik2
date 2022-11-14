
# Merke:
# Eine Variable kann genau einen Wert von einem Datentypen speichern
zahl = 1
gehalt = 1500.42
wahroderfalsch = True

# Merke:
# Eine Liste kann beliebig viele Werte von beliebig vielen Datentypen speichern
# Index                 0         1         2     3     4      5
studierendenkartei = [931589, "Kristina", "Guk", 2020, True, 120.5]

print("Die Liste studierendenkartei enthält", len(studierendenkartei), "Elemente.")
print("Am Index 1 der Studierendenkartei steht:", studierendenkartei[1])

# Iterieren des Listen-Objekts studierendenkartei und ausgeben des Inhalts
for eintraege in studierendenkartei:
    print(eintraege)


