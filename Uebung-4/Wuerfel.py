# Schreiben Sie ein Python-Programm, welches einen virtuellen Würfel mit beliebig
# vielen Seiten würfelt. Die Anzahl der Seiten soll vorher vom Nutzer eingegeben werden.
# Achten Sie auf Fehlhandlungen durch den Nutzer und fangen diese entsprechend ab.
# Gliedern Sie Ihren Code in Funktionen.

# Ein möglicher Ablauf wäre wie folgt:
#     Bitte geben Sie die Anzahl der Seiten des Würfels an: 6
#     Der Würfel rollt .........
#     Der Würfel zeigt die Zahl 4 an.

# Tipp: Nutzen Sie die `random()` Funktion, um eine zufällige Zahl zu generieren.
# Importieren Sie diese zuerst mittels `import random` und nutzen sie anschließend.
# Bspw. so: zahl = random.randint(1,10) für eine zufällige Zahl zwischen 1 und 10

import random

korrekte_eingabe = False

while not korrekte_eingabe:
    try:
        wuerfelseite = int(input("Bitte geben Sie Anzahl der Seiten des Würfels an: "))
        ergebnis = random.randint(1,wuerfelseite)
        print("Der Würfel rollt …")
        print("Der Würfel zeigt die Zahl: ", ergebnis)
        korrekte_eingabe = True
    except:
        print("Bitte geben Sie nur ganze Zahlen ein.")