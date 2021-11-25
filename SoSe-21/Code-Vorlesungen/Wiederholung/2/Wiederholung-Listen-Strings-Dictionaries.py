# #Index 0     1     2        3        4
# e = ["Das", "ist", "eine", "Liste", ["Verschachtelung", "yeah"]] # Liste
# f = {"Jonas": 2101357,
#      "Peter": 2101356} # Dictionary

einkaufsliste = []

# Definition der Funktionen
def split_nutzereingabe(eingabe):
    liste = eingabe.split(",")
    return liste

def laenge_ermitteln(liste):
    return len(liste)

def zu_liste_hinzufügen(element):
    einkaufsliste.append(element)

# Beginn der Ausführung der Funktionen
menge = int(input("Wie viele Elemente wollen Sie Ihrer Einkaufsliste hinzufügen: "))

# range(start, stop, step)
for anzahl in range(menge):
    element = input("Bitte geben Sie ein, was Sie hinzufügen wollen: ")
    zu_liste_hinzufügen(element)
print("Ihre Einkaufsliste enthält", laenge_ermitteln(einkaufsliste), "Elemente.")
print("Folgendes steht auf Ihrer Einkaufsliste:", einkaufsliste)














# nutzereingabe = input("Bitte geben Sie kommasepariert ein was Sie einkaufen müssen: ")
# einkaufsliste = split_nutzereingabe(nutzereingabe)
# print("Die Länge der Einkaufsliste beträgt:", laenge_ermitteln(einkaufsliste))

# hinzufügen = input("Wollen Sie noch etwas zu der Liste hinzufügen (ja/nein): ")
# if hinzufügen.upper() == "JA":
#     element = input("Geben Sie das Element an, was Sie hinzufügen wollen: ")
#     zu_liste_hinzufügen(element)
#     print("Das steht jetzt auf Ihrer Einkaufsliste: ", einkaufsliste)
# else:
#     print("Sie haben nichts zu Ihrer Einkaufsliste hinzugefügt.")



# löschen = input("Was wollen Sie von der Liste entfernen: ")
# liste.remove(löschen)
# print(liste)

# element = input("Was soll auf die Liste?")
# liste.append(element)
# print(liste)
