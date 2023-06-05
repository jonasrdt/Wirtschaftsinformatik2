# Erstellen Sie ein Python-Programm mit den folgenden Anforderungen.
# a) Der Anwender soll dazu aufgefordert werden, einen beliebigen Satz
# einzugeben, z. B. # „Der Hund läuft in die Küche“
# b) Erstellen Sie eine Funktion,
# welche analysiert, wie viele Wörter in dem Satz
# vorkommen.
# c) Erstellen Sie eine Funktion, welche analysiert, wie die
# durchschnittliche Wortlänge im Satz ist.

def anzahlwoerter(satz):
    # Variable satz_splitted vom Datentypen Liste (list)
    satz_splitted = satz.split(" ")
    # Verfügbar machen des Wertes hinter der Variable 'satz_splitted'
    return len(satz_splitted)

def durchschnittlicheWortlaenge(satz):
    # Ermitteln der Anzahl der Zeichen innerhalb des Satzes mithilfe der Funktion len().
    satz = satz.replace(" ", "")
    laenge_satz = len(satz)
    print("Der Satz enthält:", laenge_satz, "Zeichen.")
    # Ermitteln der durchschnittlichen Wortlänge, indem die Länge des Satzes durch
    # die Anzahl der Wörter geteilt wird.
    durchschnittliche_wortlaenge = round(laenge_satz / anzahl_woerter, 2)
    return durchschnittliche_wortlaenge

#### Hauptprogramm ####
# Variable Satz vom Datentypen String (str)
satz = input("Bitte geben Sie einen Satz ein.")

# Ermitteln der Anzahl der Wörter, in dem der Satz an die Funktion 'anzahlwoerter(satz)' übergeben
# und mittels der Funktion .split() in einzelne Wörter zerlegt wird, die dann gezählt werden.
anzahl_woerter = anzahlwoerter(satz)
print("Der Satz hat", anzahl_woerter, "Wörter.")

# Ermitteln der durchschnittlichen Wortlänge, in dem der Satz an die Funktion 'durchschnittlicheWortlaenge(satz)'
# übergeben und mittels der Funktion .replace(old, new) um die Leerzeichen bereinigt und anschließend
# die Länge des Satzes ermittelt wird.
durchschnittliche_wortlaenge = durchschnittlicheWortlaenge(satz)
print("Die durchschnittliche Wortlänge beträgt:", durchschnittliche_wortlaenge, "Zeichen.")