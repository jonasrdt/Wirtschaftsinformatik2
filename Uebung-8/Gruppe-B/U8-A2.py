# Auf dem Einwohnermeldeamt soll ein neues System implementiert werden.
# Ankommende Besucher müssen sich mit ihrem Namen anmelden. Jeder weitere
# Besucher stellt sich danach „hinten“ an. Es entsteht ein Warteschlange (Liste).
# Die Besucher werden der Reihe nach aufgerufen und verlassen die Warteschlange
# (First-In-First-Out FIFO).
# • ankommen(name) (Eine Person stellt sich in die Warteschlange hinten an)
# • verlassen() (Die erste Person einer Warteschlange verlässt die Warteschlange)
# • ausgabe() (Die komplette Warteschlange wird als Liste ausgegeben).

warteschlange = []

def ankommen(name):
    warteschlange.append(name)
    print(name, "wurde der Warteschlange am Index", len(warteschlange) - 1, "hinzugefügt.")

def verlassen():
    if len(warteschlange) > 0:
        print("Person:", warteschlange[0], "wurde aufgerufen und wird jetzt entfernt.")
        warteschlange.pop(0)
    else:
        print("Es befinden sich keine Personen in der Warteschlange.")

def ausgabe():
    if len(warteschlange) > 0:
        print("Es warten:", end=" ")
        for person in warteschlange:
            print(person, ";", end=" ")
        print()
    else:
        print("Es befinden sich keine Personen in der Warteschlange.")

def trenner(anzahl):
    for i in range(anzahl):
        print("-", end="")
    print()

##### Hauptprogramm #####
trenner(25)
ankommen("Alina")
trenner(25)
ankommen("Bernd")
trenner(25)
ankommen("Christoph")
trenner(25)
ausgabe()
trenner(25)
verlassen()
trenner(25)
verlassen()
trenner(25)
verlassen()
trenner(25)
verlassen()