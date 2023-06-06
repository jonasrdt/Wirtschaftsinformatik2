


telefonbuch = [["Christian", 2105070],
               ["Jonas", 2105071],
               ["Miriam", 2105072],
               ["Miriam"]]

for eintrag in telefonbuch:
    if len(eintrag) >= 2:
        print(eintrag[0], "hat die Telefonnummer", eintrag[1])
    elif len(eintrag) == 1:
        print("Hier ist keine Telefonnummer, sondern nur der Name", eintrag[0], "gespeichert.")
    else:
        print("Das Element ist leer.")


