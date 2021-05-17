# Aufgabe 3 in Übung 5
# Der optimale Puls bei Ausdauersportarten hängt vom Alter ab.
# Er lässt sich mit der Formel P = 165 - 0.75 * Alter bestimmen.
# 
# Schreiben Sie ein Programm, das folgenden Dialog ermöglicht:
# Alter: 18
# optimaler Puls: 151.5
# Bringen Sie die Berechnung der Formel in eine Funktion!
# Erfassen der Variablen durch eine Nutzereingabe

# Definieren von Funktionen
def optimalenPulsBerechnen(alter):
    optimaler_puls = 165 - 0.75 * alter
    return optimaler_puls

# Variablendefinition für korrekte_eingabe, um eine Schleife zu initiieren
korrekte_eingabe = False
# while Schleife die solange läuft, bis ein korrektes Alter eingegeben wurde
while not korrekte_eingabe:
    try:
        alter_nutzer = int(input("Bitte geben Sie Ihr Alter ein: "))
        if(6 <= alter_nutzer <= 105): # Abprüfen eines inhaltlichen Intervalls zwischen 6 und 105 Jahren
            korrekte_eingabe = True # Sollten alle Prüfungen erfolgreich durchlaufen sein, wird die Schleife hiermit abgebrochen
        else:
            print("Bitte geben Sie ein Alter zwischen 6 und 105 Jahren an.") # Sollte eine Eingabe erfolgen die einen Fehler erzeugt, wird dies ausgegeben
    except:
        print("Bitte geben Sie nur ganze Zahlen ein.")

# Ausführen der Funktion
print("Bei einem Alter von", alter_nutzer,"beträgt der optimale Puls für Ausdauersportarten", optimalenPulsBerechnen(alter_nutzer))