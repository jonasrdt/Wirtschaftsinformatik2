#############################################
# Technische Fehlerabfrage mit try … except
#############################################

# Setzen der Abbruchvariable
korrekte_eingabe = False
# while-Schleife läuft solange, wie noch KEINE korrekt_eingabe durchgeführt wurde
while not korrekte_eingabe:
    # Python soll VERSUCHEN den nachfolgenden Codeauszuführen
    try:
        # Nutzer auffordern eine Zahl einzugeben und diese in Integer (int) umwandeln
        alter = int(input("Bitte geben Sie Ihr Alter ein: "))
        print("Das eingegeben Alter lautet: ", alter) # wird nur ausgeführt, wenn Zeile 9 gelingt
        korrekte_eingabe = True # wird nur ausgeführt, wenn Zeile 9 und 10 gelingen
    # Auffangen der Exception, also des Fehlers
    except:
        # Ausgeben dessen, was man dem Nutzer bei einem Fehler mitteilen will
        print("Sie haben einen Buchstaben eingegeben. Bitte geben Sie nur ganze Zahlen ein.")
