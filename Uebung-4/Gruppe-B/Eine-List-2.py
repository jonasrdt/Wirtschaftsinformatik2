
einkaufsliste = ["Salat", "Tomaten", "Paprika", "Aubergine", "Chips"]

# This code is printing out the items in the list "einkaufsliste" with a hyphen in front of each item.
# The first line "print("Auf der Einkaufsliste steht: ")" is just a header to indicate that the
# following lines will be the items in the list.
print("Auf der Einkaufsliste steht: ")
for element in einkaufsliste:
    print("-", element)

# This code is asking the user to input an item they want to add to the shopping list and storing it
# in the variable "artikel". Then, it is adding the item to the end of the "einkaufsliste" using the
# "append" method.
artikel = input("Bitte geben Sie den Artikel ein, den Sie der Liste hinzufügen wollen: ")
einkaufsliste.append(artikel)
print(einkaufsliste)

artikel = input("Bitte geben Sie den Artikel ein, den Sie von der Liste entfernen wollen: ")
einkaufsliste.remove(artikel)
print(einkaufsliste)