# Variable 'einkaufsliste' vom Datentypen Liste (list)
einkaufsliste = ['Brot', 'Butter', 'Käse']

# Ausgabe aller sich auf der Einkaufsliste
# befindlichen Einträge
for eintrag in einkaufsliste:
    print("- " + eintrag)
    
# Hinzufügen zu einer Liste durch Nutzereingabe
nutzereingabe = input("Was wollen Sie zu der Liste hinzufügen: ")
# Mit .append() wird das Element hinten an die Liste angefügt
einkaufsliste.append(nutzereingabe)

# Mit .pop() wird, wenn nichts anderes übergeben wird, das letzte
# Element entfernt. Es kann aber auch ein Index übergeben werden .pop(1)
einkaufsliste.pop(1)

boardinglist = ['Claudia', 'Ute', 'Christian']
# Mit .insert() kann ein Element an einem bestimmten Index hinzugefügt werden
priority = input("Wer soll am priority boarding teilnehmen: ")
boardinglist.insert(0, priority)
print(boardinglist)