

# Index           # 0     # 1      # 2
einkaufsliste = ['Brot', 'Bier', 'Salz']

# to-do Liste
todo = []

print("Auf der to-do Liste steht:", todo)
weiteres_element = True
while weiteres_element:
    element = input("Bitte geben Sie etwas ein: ")
    todo.append(element)
    print("Auf der to-do Liste steht:", todo)
    entscheidung = input("Wollen Sie noch etwas hinzufügen (ja/nein): ")
    if entscheidung.lower() == "nein":
        weiteres_element = False
print("Sie haben folgende Elemente auf der Liste erfasst:", todo)