

def eingabe_zahl(zahl):
    gueltige_eingabe = False
    while not gueltige_eingabe:
        try:
            x = int(zahl)
            print("Vielen Dank, das war eine Zahl.")
            gueltige_eingabe = True
        except:
            print("Bitte geben Sie nur Zahlen ein.")



nutzereingabe = input("Bitte geben Sie eine Zahl ein:")
eingabe_zahl(nutzereingabe)
