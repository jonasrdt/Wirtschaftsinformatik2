warteschlange = []

def trenner(anzahl):
    for i in range(anzahl):
        print("-", end=" ")
    print()

def ankommen(name):
    try:
        warteschlange.append(name)
        print("Der Name", name, "wurde erfolgreich zur Liste hinzugefügt.")
    except:
        print("Der Name", name, "konnte nicht hinzugefügt werden.")

def verlassen():
    print(warteschlange[0], "verlässt die Warteschlange.")
    try:
        warteschlange.pop(0)
    except:
        print("Die Person konnte die Wartschlange nicht verlassen. Vermutlich, weil die Warteschlange leer ist.")

def ausgabe():
    position = 1
    print("In der Warteschlange befinden sich folgende Personen:")
    for mensch in warteschlange:
        print("An Position", position, "befindet sich:", mensch)
        position += 1
        
# Hauptprogramm
ankommen("Alina")
trenner(15)
ankommen("Bernd")
trenner(15)
ankommen("Christopher")
trenner(15)
ausgabe()
trenner(15)
verlassen()
trenner(15)
verlassen()
trenner(15)
verlassen()

