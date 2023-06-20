# Hinzufügen zu einer Liste
einkaufsliste = ["Griechischer Joghurt", "Tomaten", "Mozarella"]
print(einkaufsliste)
einkaufsliste.append("Hefeweizen")
print(einkaufsliste)

# Entfernen aus einer Liste mit .remove()
einkaufsliste.remove("Tomaten")
print(einkaufsliste)

# Entfernen aus einer Liste mit .pop()
einkaufsliste.pop() # Entfernt letztes Element
print(einkaufsliste)
einkaufsliste.pop(0) # Entfernt erstes Element, da Index 0
print(einkaufsliste)