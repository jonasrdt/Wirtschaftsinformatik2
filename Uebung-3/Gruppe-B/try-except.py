
korrekte_eingabe = False

while not korrekte_eingabe:
    # Technische Fehlerabfrage mit try,except
    try:
        alter = int(input("Bitte geben Sie Ihr Alter ein: "))
        korrekte_eingabe = True
    except:
        print("Bitte geben Sie nur Zahlen ein.")
    
print("Das von Ihnen eingebeben Alter lautet:", alter)
