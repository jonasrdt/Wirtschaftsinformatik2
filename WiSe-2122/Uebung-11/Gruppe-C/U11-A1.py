# Übung 11 - Aufgabe 1
# Mitarbeiter-Kartei
# Bereitgestellt von M. Drews im Wintersemester 2021/22

# Funktionen
def trenner(anzahl_striche):
    for i in range(anzahl_striche):
        print("-", end="")
    print()

def fehler():
    print("\nFehler: Bitte geben Sie nur Zahlen an, die zur Auswahl stehen.")    

def formular():
    global vorname, nachname, geburtsort
    vorname = input("> Vorname: ")
    nachname = input("> Nachname: ")
    geburtsort = input("> Geburtsort: ")

def suche():
    global index
    suche = input("Suchbegriff (Nachname eingeben): ")
    index = next((i for i, item in enumerate(ma_kartei) if item["Nachname"] == suche), None)

def eintrag_neu():
    
    print("\nBitte fügen Sie einen neuen Eintrag zur Mitarbeiter-Kartei hinzu: ")
    formular()
    
    gueltige_eingabe = False
    while not gueltige_eingabe:
        try:
            auswahl = int(input("\n(1) Speichern      (2) Abbrechen\n"))
            if auswahl == 1:
                gueltige_eingabe = True
                eintrag = {"Vorname": vorname,"Nachname": nachname,"Geburtsort": geburtsort}
                ma_kartei.append(eintrag)
                print("Ihr Eintrag wurde gespeichert und der Kartei hinzugefügt.")
                trenner(80)        
            elif auswahl == 2:
                gueltige_eingabe = True
        except:
            fehler()  


def eintrag_bearbeiten():
    print("Welchen Eintrag möchten Sie bearbeiten?")
    suche()
    print("\nBitte überschreiben Sie den alten Eintrag:")
    formular()
    ma_kartei[index] = {"Vorname": vorname,"Nachname": nachname,"Geburtsort": geburtsort}

    print("Ihr Eintrag wurde gespeichert und der Kartei hinzugefügt.")
    trenner(80)


def eintrag_loeschen():
    print("Welchen Eintrag möchten Sie löschen?")
    suche()
    print("\nFolgender Eintrag wurde gelöscht:")
    print(ma_kartei[index])
    ma_kartei.pop(index)


# Programmablauf
print("\n")
trenner(120)
print("Mitarbeiter-Kartei")
trenner(120)
trenner(120)

ma_kartei = []

programm = True
while programm:
    print("Was möchten Sie tun?")
    gueltige_eingabe = False
    while not gueltige_eingabe:
        try:
            auswahl = int(input("\n(1) Eintrag hinzufügen\n(2) Eintrag bearbeiten\n(3) Eintrag löschen\n(4) Kartei anzeigen\n"))
            if auswahl == 1:
                gueltige_eingabe = True
                eintrag_neu()
            elif auswahl == 2:
                gueltige_eingabe = True
                eintrag_bearbeiten()
            elif auswahl == 3:
                gueltige_eingabe = True
                eintrag_loeschen()
            elif auswahl == 4:
                gueltige_eingabe = True
                print(ma_kartei)
                trenner(80)
        except:
            fehler()
