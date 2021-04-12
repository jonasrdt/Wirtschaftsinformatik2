# Aufgabe 3 - Übung 3
#
# Erstellen Sie ein Python-Programm mit den folgenden Anforderungen:
# • Der Anwender soll dazu aufgefordert werden, sein monatliches Bruttogehalt
# einzugeben.
# • Liegt das Gehalt über 2.500 €, sind 22% Steuern zu zahlen, ansonsten 18%.
# • Innerhalb des Programms soll anhand des Gehalts entschieden werden, welcher
# Steuersatz zur Anwendung kommt.
#

# Festlegen der Steuersätze
hoechstSatz = 0.22
normalerSatz = 0.18

# Erfassung der Nutzereingabe
bruttogehalt = float(input("Bitte geben Sie Ihr Bruttogehalt ein:"))

# Verarbeitung der Eingabe und Entscheidung über den Steuersatz

if bruttogehalt > 2.500:
    steuern = bruttogehalt * hoechstSatz
    print("In Ihrem Gehalt i.H.v.", bruttogehalt, "sind", steuern, "Steuern enthalten.")
elif bruttogehalt < 2.500:
    steuern = bruttogehalt * normalerSatz
    print("In Ihrem Gehalt i.H.v.", bruttogehalt, "sind", steuern, "Steuern enthalten.")
else:
    print("Der Steuersatz nicht berechnet werden kann.")