# Aufgabe 10
# Ermitteln Sie die Anzahl der Wörter in einer
# Nutzereingabe und die durchschnittliche Wortlänge.

def anzahlwoerter(nutzereingabe):
    nutzereingabe_splitted = nutzereingabe.split(" ")
    return nutzereingabe_splitted

def wortlaenge(nutzereingabe, nutzereingabe_splitted):
    durchschnittliche_wortlaenge = len(nutzereingabe) / len(nutzereingabe_splitted)
    return durchschnittliche_wortlaenge


nutzereingabe = input("Bitte geben Sie einen Satz ein: ")
gesplittete_nutzereingabe = anzahlwoerter(nutzereingabe)
print("Die Anzahl der Wörter in Ihrem Satz ist:", len(gesplittete_nutzereingabe))
print("Die durchschnittliche Wortanzahl beträgt:", wortlaenge(nutzereingabe, gesplittete_nutzereingabe), "Zeichen.")