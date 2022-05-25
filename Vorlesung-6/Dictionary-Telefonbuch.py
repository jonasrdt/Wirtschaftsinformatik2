telefonbuch = {
    # Key               # Value
    'Jonas Reinhardt': '043121021324',
    'Sahand Fathiroshan': '01525898232938',
    'Peter Mustermann': '0176287842342'
}

# Ausgeben aller Namen im Telefonbuch
print("Im Telefonbuch befinden sich:", telefonbuch.keys())
suche = input("Wessen Telefonnummer wollen Sie ändern: ")

# Membership Operator "in" prüft ob der Name in dem Telefonbuch vorkommt
if suche in telefonbuch:
    print("Der Name", suche, "ist vorhanden.")
    neue_nummer = input("Bitte geben Sie die neue Telefonnummer ein: ")
    # Ändern der bestehenden Nummer
    telefonbuch.update({suche: neue_nummer})
    print("Die neue Nummer wurde gespeichert:", telefonbuch[suche])
else:
    print("Der Name", suche, "ist nicht vorhanden.")
    # Wenn der Eintrag nicht vorhanden ist, kann er hinzugefügt werden
    hinzufuegen = input("Wollen Sie den Namen hinzufügen (ja/nein): ")
    if hinzufuegen.lower() == "ja":
        nummer_neuer_kontakt = input("Bitte geben Sie die zugehörige Telefonnummer ein: ")
        telefonbuch.update({suche: nummer_neuer_kontakt})
        print("Der Kontakt", suche ,"wurde mit der Nummer gespeichert:", telefonbuch[suche])
        print(telefonbuch)
