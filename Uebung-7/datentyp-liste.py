


a = 5       # int
b = 5.5     # float
c = "Jonas" # String

# paris = ['Frankreich', 2.161]
# paris.pop() # Entfernt das letzte hinzugefügte Element (2.161)
# paris.pop(0) # Entfernt das Element am Index 1 (Frankreich)


                # String   # String  # String
einkaufsliste = ['Banane', 'Apfel', 'Milch'] # Liste
print("Auf der Einkaufsliste steht: ", einkaufsliste)
einkaufsliste.append('Bier') # Fügt das Element 'Bier' oben auf den Stapel ein
print("Auf der Einkaufsliste steht: ", einkaufsliste)
einkaufsliste.insert(0, 'Mehl') # Fügt das Element 'Mehl' am Index 0 ein
print("Auf der Einkaufsliste steht: ", einkaufsliste)

städte = [['Paris', 2.161], # Paris steht am Index 0
          ['Berlin', 3.645], # Berlin steht am Index 1
          ['Athen', 3.161]] # Athen steht am Index 2

for stadt in städte:
    print("In der Liste steht die Stadt:", stadt[0], "mit", stadt[1], "Einwohnern.")


