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
def berecheneOptimalerPuls(alter):
    optimaler_puls = int(165 - 0.75 * alter)
    return optimaler_puls

# Grundsätzlich, gehen wir von einer falschen Eingabe aus
korrekte_eingabe = False

# Solange wie keine gültige Eingabe erfolgt ist, wird diese Schleife ausgeführt
while not korrekte_eingabe:
    try:
        alter_nutzer = int(input("Bitte geben Sie Ihr Alter ein: ")) # Versuchen eine Nutzereingabe zu erhalten
        if (6 <= alter_nutzer <= 105): # Bedingung, dass das Alter größer sein muss als 6
            korrekte_eingabe = True # Abbruchbedingung für die while-Schleife
        else:
            print("Bitte geben Sie ein Alter zwischen 6 und 105 Jahren ein.")
    except:
        print("Bitte geben Sie ein gültiges Alter in Form einer Zahl ein: ") # Zu neuer Eingabe auffordern, wenn Eingabe ungültig war

# Ausgabe der berechneten Werte
print("Bei einem Alter von", alter_nutzer, "beträgt der optimale Puls für Ausdauersportarten:", berecheneOptimalerPuls(alter_nutzer))
