# Schreiben Sie ein Python Programm, mithilfe dessen Sie eine Mitarbeiter-Kartei anlegen und diese
# im Anschluss bearbeiten/löschen können. Teil dieser Mitarbeiter-Kartei sollen: Vorname, Name, Geburtsort, Alter,
# Familienstand und die Telefonnummer sein. 

def zahl(platzhalter, datentyp):
    """
    It asks the user to enter a number, and returns the number if it's an integer or float
    
    :param platzhalter: This is the placeholder for the input
    :param datentyp: The type of data you want to return
    :return: the variable zahl.
    """
    richtige_eingabe = False
    while not richtige_eingabe:
        try:
            print("Bitte geben Sie", platzhalter, "ein.")
            zahl = datentyp(input("Eingabe: ")) # Lokale Variable, nicht von außen abrufbar!
            richtige_eingabe = True
        except:
            print("Bitte geben Sie nur ganze Zahlen ein.")
    return zahl

def strassenname():
    """
    The function strassenname() asks the user to input a street name and checks if the input is a
    string. If it is, the function returns the street name. If it isn't, the function asks the user to
    input a street name again.
    :return: the street name.
    """
    richtige_strasse = False
    while not richtige_strasse:
        strasse = input("Bitte geben Sie die Straße ein: ")
        if (strasse.isalpha()):
            richtige_strasse = True
            return strasse
        else:
            print("Bitte geben Sie NUR die Straße OHNE die Hausnummer ein.")    

# Initialisieren des Dictionaries MA Kartei
mitarbeiterkartei = {}

# Abfragen des Namens und aufteilen in Vor- und Nachname
name = input("Bitte geben Sie Ihren vollständigen Namen ein: ")
name_splitted = name.split(" ")
vorname = name_splitted[0]
nachname = name_splitted[1]
print("Der gespeicherte Vorname lautet:", vorname)
print("Der gespeicherte Nachname lautet:", nachname)
# Abfrage des Geburtsortes
geburtsort = input("Bitte geben Sie Ihren Geburtsort ein: ")
# Abfrage des Alters mithilfe der Funktion zahl()
alter = zahl("Ihr Alter", int)
# Abfragen der Straße und Hausnummer
strasse = strassenname()
hausnummer = zahl("Ihre Hausnummer", int)
# Abfragen des Familienstandes
familienstand = input("Bitte geben Sie einen Familienstand an: ")
telefonnummer = input("Bitte geben Sie Ihre Telefonnummer ein: ")

mitarbeiterkartei.update({"Vorname": vorname, 
                          "Nachname": nachname,
                          "Geburtsort": geburtsort,
                          "Alter": alter,
                          "Straße": strasse,
                          "Hausnummer": hausnummer,
                          "Familienstand": familienstand,
                          "Telefonnummer": telefonnummer
                          })
print(mitarbeiterkartei)