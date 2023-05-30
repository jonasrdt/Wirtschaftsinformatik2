# Ergänzen Sie den nachfolgenden Code so, dass der User einen beliebigen Artikel sowie
# eine Menge eingeben kann, die zu dem Dictionary `einkaufsliste` hinzugefügt wird.
# Eine Behandlung von Fehlern ist nicht notwendig. Gehen Sie davon aus, dass der User
# eine saubere Eingabe tätigt.


einkaufsliste = {"Brot": 5,
                 "Wasser": 2}

artikel = input("Bitte geben Sie einen Artikel ein: ")
menge = int(input("Bitte geben Sie eine Menge ein: "))
einkaufsliste[artikel] = menge

# Gleiches Ergebnis wie in Zeile 12. It's up to you…
# einkaufsliste.update({artikel: menge})

