
# Erstellen Sie ein Pascal'sches Dreieck

zaehlvariable = 9

for auesserer_zaehler in range(1, zaehlvariable+1):
    for leerzeichen in range(zaehlvariable-auesserer_zaehler, 0, -1):
        print(" ", end=" ")
    for innerer_zaehler_hoch in range(1,auesserer_zaehler+1):
        print(innerer_zaehler_hoch, end=" ")
    for innerer_zaehler_runter in range(auesserer_zaehler-1, 0, -1):
        print(innerer_zaehler_runter, end=" ")
    print()
