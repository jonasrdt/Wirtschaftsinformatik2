

a = 27
b = 1.55412
c = True
d = "Test"
e = ["Test", 2, True, "Bla Bla", 1.84]

beispiel_liste = [["Jonas", 28],
                  ["Jasper", 24],
                  ["Laura", 25]]

beispiel_dict = {"Jonas": 28,
                "Jasper": 24,
                "Laura": 25}

# Alter von Jasper mit Dict
print(beispiel_dict["Laura"])

# Alter von Jasper mit Liste
for zeilen in beispiel_liste:
    if zeilen[0] == "Laura":
        print(zeilen[1])
