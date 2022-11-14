# It creates a list with the items "Bier", "Tortilla Chips" and "Käse Dip".
einkaufsliste = ["Bier", "Tortilla Chips", "Käse Dip"]
print("Auf der Einkaufsliste steht:", einkaufsliste)

# It adds the item "Haribo Frösche" to the end of the list.
einkaufsliste.append("Haribo Frösche")
print("Auf der Einkaufsliste steht:", einkaufsliste)

# It removes the item "Käse Dip" from the list and adds the item "Salsa Dip" to the list.
einkaufsliste.remove("Käse Dip")
einkaufsliste.append("Salsa Dip")
print("Auf der Einkaufsliste steht:", einkaufsliste)

# It inserts the item "Möhren" at the beginning of the list.
einkaufsliste.insert(0, "Möhren")
print("Auf der Einkaufsliste steht:", einkaufsliste)
