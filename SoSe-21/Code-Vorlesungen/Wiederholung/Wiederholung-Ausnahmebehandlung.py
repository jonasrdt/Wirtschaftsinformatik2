print("Willkommen auf der Seite der Flensburger Brauerei.")
print("Bitte geben Sie Ihr Alter zur Verifikation ein.")

# Ändern des Datentypen von 'string' in 'int', damit wir damit rechnen können
gueltige_eingabe = False
while not gueltige_eingabe:
    # Mithilfe von try,except technisch prüfen, ob ein 'int' kommt oder nicht
    try:
        alter = int(input("Bitte geben Sie Ihr Alter ein: "))
        # Inhaltliche Prüfung der Eingabe
        if alter >= 16:
            gueltige_eingabe = True
        else:
            print("Diese Seite ist nur für Personen über 16 Jahren geeignet.")
    except:
        print("Bitte geben Sie nur Zahlen für Ihr Alter ein.")
