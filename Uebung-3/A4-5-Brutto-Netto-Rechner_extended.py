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
ledig = 0.26
verheiratet = 0.22
ermaessigung = 0.04

# Erfassung der Nutzereingabe
bruttogehalt = float(input("Bitte geben Sie Ihr Bruttogehalt ein:"))
familienstand = input("Bitte geben Sie an, ob Sie ledig oder verheiratet sind: ")

# Verarbeitung der Eingabe und Entscheidung über den Steuersatz

if bruttogehalt > 4.000 and familienstand.lower() == "ledig":
    steuern = bruttogehalt * ledig
    print("In Ihrem Gehalt i.H.v.", bruttogehalt, "sind", steuern, "Steuern enthalten.")
elif bruttogehalt > 4.000 and familienstand.lower() == "verheiratet":
    steuern = bruttogehalt * verheiratet
    print("In Ihrem Gehalt i.H.v.", bruttogehalt, "sind", steuern, "Steuern enthalten.")
elif bruttogehalt <= 4.000 and familienstand.lower() == "ledig":
    steuern = bruttogehalt * (ledig - ermaessigung)
    print("In Ihrem Gehalt i.H.v.", bruttogehalt, "sind", steuern, "Steuern enthalten.")
elif bruttogehalt <= 4.000 and familienstand.lower() == "verheirtatet":
    steuern = bruttogehalt * (verheiratet - ermaessigung)
    print("In Ihrem Gehalt i.H.v.", bruttogehalt, "sind", steuern, "Steuern enthalten.")
else:
    print("Der Steuersatz nicht berechnet werden kann.")