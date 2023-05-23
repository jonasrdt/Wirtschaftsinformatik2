# Schreiben Sie ein Programm, mithilfe dessen der User eine
# to-do Liste erstellen kann. Er soll hierbei Einträge verfassen
# und diese mit einer Priorität(1-99) speichern können.
# Achten Sie auf Fehleingaben durch den Nutzer.
# Der Nutzer kann solange to-dos eingeben, bis er "Nein" eingibt.

# Bonus: Geben Sie die to-do Liste nach jeder erfolgreichen
# Eingabe untereinander aus.

todoliste = []

weitere_eingabe = True
while weitere_eingabe:
# This code block is prompting the user to enter a to-do item and a priority for that item. It first
# uses the `input()` function to prompt the user with the message "Bitte geben Sie ein to-do ein: "
# and stores their response in the variable `todo`. It then sets the variable `korrekte_eingabe` to
# `False` to indicate that the user has not yet entered a valid priority. It enters a while loop that
# will continue until the user enters a valid priority. Within the while loop, it uses the `int()`
# function to convert the user's input to an integer and stores it in the variable `prio`. If the user
# enters a non-integer value, the `except` block is executed and the message "Bitte geben Sie nur
# Zahlen ein:" is printed to the console. Once the user enters a valid priority, `korrekte_eingabe` is
# set to `True` and the to-do item and priority are appended to the `todoliste` list as a sublist
# `[todo, prio]`.
    todo = input("Bitte geben Sie ein to-do ein: ")
    korrekte_eingabe = False
    while not korrekte_eingabe:
        try:
            prio = int(input("Bitte geben Sie die Priorität (1-99) ein: "))
            korrekte_eingabe = True
        except:
            print("Bitte geben Sie nur Zahlen ein:")
    #                   0     1
    todoliste.append([todo, prio])
    
# This code block is printing the current to-do list after each successful entry. It first prints a
# header "Auf der Liste steht aktuell:" and then iterates through the `todoliste` list using a for
# loop. For each entry in the list, it prints a bullet point "-", followed by the to-do item
# (`eintrag[0]`) and its priority (`eintrag[1]`). Finally, it prints a line of dashes as a separator.
    print("Auf der Liste steht aktuell:")
    for eintrag in todoliste:
        print("-", eintrag[0], "mit der Prio", eintrag[1])
    print("------------------------------------")
    
# This code block is asking the user if they want to make another entry in the to-do list. It uses the
# `input()` function to prompt the user with the question "Wollen Sie eine weitere Eingabe tätigen
# (ja/nein): " and stores their response in the variable `entscheidung`.
    entscheidung = input("Wollen Sie eine weitere Eingabe tätigen (ja/nein): ")
    if entscheidung.lower() == "nein":
        weitere_eingabe = False

print(todoliste)