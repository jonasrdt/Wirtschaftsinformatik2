

eingabe_1 = input("Wählen Sie Stein, Schere oder Papier: ")
eingabe_2 = input("Wählen Sie Stein, Schere oder Papier: ")

if (eingabe_1.lower() == "schere" and eingabe_2.lower() == "papier"):
    print("Spieler 1 hat gewonnen.")
elif (eingabe_1.lower() == "papier" and eingabe_2.lower() == "stein"):
    print("Spieler 1 hat gewonnen.")
