# Login-Maske
# Variablendefinition
passwort = "Aligator123"
richtiges_passwort = False
versuche = 3

# Hauptprogramm
while not richtiges_passwort and versuche >= 0:
    nutzer_eingabe = input("Bitte geben Sie das Passwort ein (achten Sie auf Groß- und Kleinschreibung): ")
    if nutzer_eingabe == passwort:
        print("Herzlichen Glückwünsch, Sie haben sich erfolgreich eingeloggt.")
        richtiges_passwort = True
    else:
        print("Das Passwort war leider nicht richtig. Bitte versuchen Sie es erneut.")
        print("Sie haben noch", versuche, "Versuche.")
        versuche -= 1

if versuche <= 0:
    print("Sie haben alle Versuche für die Eingabe verbraucht. Bitte setzen Sie Ihr Passwort zurück.")