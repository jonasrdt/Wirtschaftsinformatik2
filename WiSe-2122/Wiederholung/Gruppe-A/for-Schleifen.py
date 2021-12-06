
 
namen = [["Moritz", "Müller", "Kiel", "24", "ledig"],
         ["Alina", "Musterfrau", "Hamburg", "21"],
         ["Niklas", "Hansen", "Lübeck", "26", "Fußballspieler"],
         ["Synthia", "Jensen", "Schleswig", "20"]]

for element in range(len(namen)):
    print("Der Vorname lautet: \t", namen[element][0], "\nDer Nachname lautet: \t", namen[element][1])
    print("Die Person hat folgende weitere Attribute: ")
    for attribut in range(len(namen[element])):
        if attribut >= 2:
            print(namen[element][attribut])
    print()