richtige_eingabe = False
while not richtige_eingabe:
    try:
        zahl = int(input("Bitte geben Sie eine ganze Zahl ein: "))
        richtige_eingabe = True
        if zahl % 2 == 0:
            print("gerade")
        else:
            print("Die von Ihnen eingegebene Zahl ist ungerade.")
    except:
        print("Bitte geben Sie nur ganze Zahlen ein.")