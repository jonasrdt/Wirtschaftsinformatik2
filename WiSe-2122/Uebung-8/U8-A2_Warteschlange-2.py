# Im Einwohnermeldeamt soll ein neues System implementiert werden.
# Ankommende Besucher müssen sich mit ihrem Namen anmelden. Jeder weitere Besucher stellt sich danach
# „hinten“ an. Es entsteht ein Warteschlange (Liste). Die Besucher werden der Reihe nach aufgerufen
# und verlassen die Warteschlange (First-In-First-Out FIFO).

# Programmieren Sie eine Warteschlange mit folgenden Funktionen:
# • ankommen(name) (Eine Person stellt sich in die Warteschlange hinten an)
# • verlassen() (Die erste Person einer Warteschlange verlässt die Warteschlange)
# • ausgabe() (Die komplette Warteschlange wird als Liste ausgegeben).

warteschlange = []

def ankommen(name):
    warteschlange.append(name)
    print(name, "wurde zur Wartschlange hinzugefügt.")

def verlassen(name):
    print(warteschlange[0], "hat die Warteschlange verlassen.")
    warteschlange.pop(0)

def ausgabe():
    print("Die Warteschlange enthält: ", warteschlange)

ankommen("Jonas")
ankommen("Peter")
ankommen("Willi")
ausgabe()
verlassen()
ausgabe()
verlassen()
ausgabe()