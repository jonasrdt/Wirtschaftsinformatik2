# Variablen von einem Datentypen die nur einen Wert halten können
zahl = 1                # Integer
einkommen = 1555.22     # Float
schwanger = True        # Boolean

# Besondere Variable, die mehrere Werte von mehreren Datentypen halten kann
# Index                 0        1         2        3           4      5
studierendenkartei = [931589, "Uluyol", "Miray", "WiSe 19/20", True, 95.5]

# Direkter Zugriff über Index
print("In der Studierendekartei befinden sich", len(studierendenkartei), "Elemente.")
print(studierendenkartei[3])

# Iterieren über die Liste studierendenkartei mithilfe des Membership Operators "in"
for elements in studierendenkartei:
    print(elements)