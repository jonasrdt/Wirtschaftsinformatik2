
# Dictionary ist ein Key Value Store
todo = {}


# Funktionsdefinition
def wichtigkeit():
    """
    The function asks the user to input the importance of the task. The input is then added to the
    dictionary as a value
    """
    todo_wichtigkeit = input("Bitte geben Sie die Wichtigkeit ein (Wichtig/Mittelwichtig/Unwichtig): ")
    todo.update({todo_eintrag.capitalize(): todo_wichtigkeit}) 

def schleifenabbruch():
    """
    It asks the user if they want to write another entry. If they say no, it returns False
    :return: the boolean value False.
    """
    entscheidung = input("Wollen Sie einen weiteren Eintrag verfassen (ja/nein): ")
    if entscheidung.lower() == "nein":
        return False
    if entscheidung.lower() == "ja":
        return True

    
    
########################
##### Hauptprogramm ####
########################
weiterer_eintrag = True
while weiterer_eintrag:
    todo_eintrag = input("Bitte geben Sie ein todo ein: ")
    
    if todo_eintrag.capitalize() in todo:
        ueberschreiben = input("Der Eintrag ist doppelt. Wollen Sie den bestehenden Eintrag überschreiben (ja/nein): ")
        if ueberschreiben.lower() == "ja":
            wichtigkeit()
        else:
            weiterer_eintrag = schleifenabbruch()
    else:           
        wichtigkeit()
        weiterer_eintrag = schleifenabbruch()
print(todo)