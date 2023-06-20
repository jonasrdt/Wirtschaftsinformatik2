
# einkaufsliste mit Datentyp Dictionary
einkaufsliste = {"Griechischer Joghurt": 1,
                 "Mozarella": 2,
                 "Tomaten": 5}

# Erste Möglichkeit, um etwas zu einem Dictionary hinzuzufügen oder zu ändern
einkaufsliste.update({"Hefeweizen": 5})
print(einkaufsliste)

# Zweite Möglichkeit, um etwas zu einem Dictionary hinzuzufügen oder zu ändern
einkaufsliste["Kräuterbutter"] = 1
print(einkaufsliste)

# Entfernen eines Elements mit .pop()
# Nicht verwechseln: Bei Liste braucht .pop() einen Index bspw. 0
#                    Bei Diciontary braucht .pop einen Key bspw. "Mozarella"
einkaufsliste.pop("Mozarella")
print(einkaufsliste)