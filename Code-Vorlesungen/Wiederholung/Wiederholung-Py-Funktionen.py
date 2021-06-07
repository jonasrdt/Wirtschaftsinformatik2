adressbuch = {"JONAS": 123456,
            "PETER": 8765435}

gesuchter_kontakt = input("Bitte geben Sie den Kontakt ein, den Sie suchen: ").upper() # JONAS

if gesuchter_kontakt in adressbuch:   
    print("Die Telefonnummer von", gesuchter_kontakt ,"ist:", adressbuch[gesuchter_kontakt])
else:
    print("Dieser Eintrag ist nicht vorhanden.")


for zaehler in range(11):
    print(zaehler)