##### Extra Aufgabe 1 #####
# Ein Nutzer soll eine Einkaufsliste erstellen.
# Zu dieser Einkaufsliste sollen beliebig viele Elemente hinzugefügt werden
# Der Nutzer soll auch die Möglichkeit haben, Elemente von dort zu löschen.

einkaufsliste = []

abbruchbedingung = False

while not abbruchbedingung:
    nutzereingabe = input("Bitte geben Sie ein, was Sie der Einkaufsliste hinzufügen wollen: ")
    einkaufsliste.append(nutzereingabe)
    weitermachen = input("Möchten Sie noch mehr hinzufügen (ja/nein): ")
    if weitermachen.lower() == "nein":
        abbruchbedingung = True

print("Auf der Einkaufsliste steht: ", einkaufsliste)
entfernen = input("Möchten Sie eines der Elemente entfernen (ja/nein): ")
if entfernen.lower() == "ja":
    print("Auf der Liste steht aktuell: ", einkaufsliste)
    element_entfernt = False
    while not element_entfernt:
        element = input("Welches Element wollen Sie aus der Liste entfernen: ")
        if element in einkaufsliste:
            einkaufsliste.remove(element)
            print(element, "wurde erfolgreich entfernt.")
            element_entfernt = True
        else:
            print("Das Element befindet sich nicht auf der Liste.")

print("Auf der Einkaufsliste steht: ", einkaufsliste)