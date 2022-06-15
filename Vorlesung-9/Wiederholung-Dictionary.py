
# Dictionary ist ein Key Value Store
todo = {}

weiterer_eintrag = True
while weiterer_eintrag:
    todo_eintrag = input("Bitte geben Sie ein todo ein: ")
    
    if todo_eintrag in todo:
        ueberschreiben = input("Der Eintrag ist doppelt. Wollen Sie den bestehenden Eintrag überschreiben (ja/nein): ")
        if ueberschreiben.lower() == "ja":
            todo_wichtigkeit = input("Bitte geben Sie die Wichtigkeit ein (Wichtig/Mittelwichtig/Unwichtig): ")
            todo.update({todo_eintrag: todo_wichtigkeit})
        else:
            entscheidung = input("Wollen Sie einen weiteren Eintrag verfassen (ja/nein): ")
            if entscheidung.lower() == "nein":
                weiterer_eintrag = False
    else:           
        todo_wichtigkeit = input("Bitte geben Sie die Wichtigkeit ein (Wichtig/Mittelwichtig/Unwichtig): ")
        todo.update({todo_eintrag: todo_wichtigkeit}) 
          
        entscheidung = input("Wollen Sie einen weiteren Eintrag verfassen (ja/nein): ")
        if entscheidung.lower() == "nein":
            weiterer_eintrag = False
print(todo)