# Schreiben Sie ein Python-Programm, welches einen virtuellen Würfel mit beliebig
# vielen Seiten würfelt. Die Anzahl der Seiten soll vorher vom Nutzer eingegeben werden.
# Achten Sie auf Fehlhandlungen durch den Nutzer und fangen diese entsprechend ab.
# Gliedern Sie Ihren Code in Funktionen.

#     Ein möglicher Ablauf wäre wie folgt:
#     Bitte geben Sie die Anzahl der Seiten des Würfels an: 6
#     Der Würfel rollt .........
#     Der Würfel zeigt die Zahl 4 an.

# Tipp: Nutzen Sie die `random()` Funktion, um eine zufällige Zahl zu generieren.
# Importieren Sie diese zuerst mittels `import random` und nutzen sie anschließend.
# Bspw. so: zahl = random.randint(1,10) für eine zufällige Zahl zwischen 1 und 10

import random

nochmal_wuerfeln = "ja"

while nochmal_wuerfeln.lower() == "ja":
    try:
        seitenzahl = int(input("Bitte geben Sie die Anzahl der Würfelseiten ein: "))
        ergebnis = random.randint(1, seitenzahl)
        print("Der Würfel rollt .....")
        print("Der Würfel zeigt die Zahl", ergebnis, "an.")
        nochmal_wuerfeln = input("Wollen Sie noch Mal würfeln (ja/nein): ")
    except:
        print("Bitte nur ganze Zahlen eingeben. Es ist schließlich ein Würfel.")
