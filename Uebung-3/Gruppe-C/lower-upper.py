

print("Willkommen beim Hotel Holiday - Bitte registrieren Sie sich")
print("----------------------------------------------------")
vorname = input("Bitte geben Sie Ihren Vornamen ein: ")
nachname = input("Bitte geben Sie Ihren Nachnamen ein: ")

vorname = vorname.lower() # alle Buchstaben kleinschreiben
print("Vorname:", vorname)
vorname = vorname.capitalize() # nur den Anfangsbuchstaben großschreiben
print("Vorname:", vorname)

nachname = nachname.lower() # alle Buchstaben kleinschreiben
print("Nachname", nachname)
nachname = nachname.capitalize() # nur den Anfangsbuchstaben großschreiben
print("Nachname", nachname)

print("Herzlich Willkommen Herr", vorname, nachname)

if (nachname == "Reinhardt" and vorname == "Jonas"):
    print("Sie sind bereits registriert.")
else:
    print("Sie haben sich noch nicht registriert.")