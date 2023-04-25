

korrekte_eingabe = False

while not korrekte_eingabe:
    try: 
        zeilen_anzahl = int(input("Bitte geben Sie die Anzahl der Zeilen ein: "))
        spalten_anzahl = int(input("Bitte geben Sie die Anzahl der Spalten ein: "))
        zeichen = input("Bitte gib das Zeichen an, aus dem die Matrix gebaut werden soll: ")

        for zeilen in range(zeilen_anzahl):
            for spalten in range(spalten_anzahl):
                print(zeichen, end =" ")
            print()
    except:
        print("Bitte nur Zahlen eingeben.")