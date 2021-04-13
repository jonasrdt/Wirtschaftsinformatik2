# Aufgabe 3 - Übung 5
#
# Der optimale Puls bei Ausdauersportarten hängt vom Alter ab.
# Er lässt sich mit der Formel P = 165 - 0.75 * Alter bestimmen.
#
# Schreiben Sie ein Programm, das folgenden Dialog ermöglicht:
# # Alter: 18
# # optimaler Puls: 151.5
# Bringen Sie die Berechnung der Formel in eine Funktion!


# Begrüßung des Nutzers
print()
print ("Mithilfe dieses Programms können Sie Ihren optimalen Puls für Ausdauersportarten berechnen.")

# Erfassen der Nutzereingabe
print ("Bitte geben Sie hierzu nachfolgend Ihr Alter ein.")
print()

# Abfangen von Fehleingaben, bspw. durch Buchstaben
gueltige_eingabe = False
while not gueltige_eingabe:
    try: 
        alter = int(input("Mein Alter beträgt: "))
        print ("Das von Ihnen eingegeben Alter lautet: ", alter)
        gueltige_eingabe = True
    except:
        print("Bitte geben Sie nur Zahlen für Ihr Alter ein.")

# Definieren der Funktion zur Verarbeitung der Nutzereingabe
def optimalerPuls (alter):
    p = 165 - 0.75 * alter
    return int(p)

# Verarbeiten der Nutzereingabe
berechneter_Puls = optimalerPuls(alter)

# Ausgabe der Berechnung
print()
print ("Mit einem Alter von", alter, "liegt Ihr optimaler Puls für Ausdauersportarten bei", berechneter_Puls, ".")
print()



