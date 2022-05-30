
stueckliste = []

weiteres_bauteil = True
while weiteres_bauteil:
    bauteil = input("Bitte geben Sie ein Bauteil ein: ")
    
    # Abbruchbedingung für die innere While Schleife
    richtige_eingabe = False
    while not richtige_eingabe:
        try:
            menge = int(input("Bitte geben Sie die Menge für das Bauteil ein: "))
            richtige_eingabe = True
            stueckliste.append([bauteil, menge])
        except:
            print("Bitte nur ganze Zahlen für die Menge erfassen.")
    
    # Abbruchbedingung für die äußere While-Schleife
    entscheidung = input("Wollen Sie noch ein Bauteil hinzufügen (ja/nein): ")
    if entscheidung.lower() == "nein":
        weiteres_bauteil = False
        
print("Auf der Stückliste stehen folgende Elemente:")
for element in stueckliste:
    print("Bauteil:\t", element[0], "\n", "Menge:\t\t", element[1])
    print("----------------------------")
