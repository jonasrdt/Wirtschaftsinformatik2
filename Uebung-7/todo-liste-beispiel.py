# Variablendefinition und Initialisieren des Listenelements
todo_liste = []

# Funktionsdefinition
def addToDoList():
    todo = input("Bitte geben Sie ein to-do ein: ")
    todo_liste.append(todo)
    print("Auf der Liste befindet sich aktuell:", todo_liste)

def removeToDoList():
    richtiges_element = False
    while not richtiges_element:
        print("Auf der Liste befindet sich", todo_liste)
        element_entfernen = input("Welches Element der Liste wollen Sie entfernen: ")
        try:
            todo_liste.remove(element_entfernen)
            print("Element", element_entfernen, "wurde erfolgreich entfernt.")
            print("Die aktuelle Liste sieht so aus: ", todo_liste)
            richtiges_element = True
        except:
            print(element_entfernen, "befindet sich nicht auf der Liste.")

# Hauptprogramm
if len(todo_liste) == 0:
    print("Ihre todo Liste ist aktuell leer.")
    entscheidung = input("Möchten Sie etwas hinzufügen (ja/nein): ")
    if entscheidung.lower() == "ja":
        weitermachen = True
        while weitermachen:
            addToDoList()
            weitermachen_entscheidung = input("Wollen Sie noch etwas hinzufügen (ja/nein: ")
            if weitermachen_entscheidung.lower() == "nein":
                weitermachen = False
else:
    print("Auf der Liste befinden sich folgende to-dos: ", todo_liste)

will_entfernen = input("Wollen Sie ein Element löschen (ja/nein): ")
if will_entfernen.lower() == "ja":
    removeToDoList()