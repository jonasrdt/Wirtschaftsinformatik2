
vornamen = [["Julia", "Birkemeyer", "Kiel", "25"],
            ["Mark", "Hubrich", "Hamburg", "22"],
            ["Anna-Lena", "Hagemann", "Lübeck", "26"],
            ["Thorben", "Walter", "Schleswig", "21"]]


for name in range(len(vornamen)):
    print("Der Vorname lautet: \t", vornamen[name][0], "\nDer Nachname lautet: \t", vornamen[name][1])
    print("Weitere Attribute zu dem Datensatz lauten: ")
    for attribute in range(len(vornamen[name])):
        if attribute >= 2:
            print(vornamen[name][attribute])