



gueltige_groesse = False
while not gueltige_groesse:
    try:
        groesse = float(input("Bitte geben Sie Ihre Größe cm ein:"))
        if groesse > 240:
                print("Bitte geben Sie eine realistische Größe ein.")
        else:
            gueltige_groesse = True
    except:
        print("Bitte geben Sie nur Zahlen ein!")