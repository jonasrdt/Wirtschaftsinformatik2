

# Schreiben Sie ein Python-Programm, welches solange ganze Zahlen vom Nutzer entgegennimmt
# bis dieser etwas anderes eingibt. Anschließend soll das Programm die Summe
# der Zahlen ausgeben. Achten Sie hierbei nicht Fehlerabfragen.
summe = 0

correct_input = False
while not correct_input:
    zahl = input("Zahl: ")
    try:
        summe += int(zahl)
    except:
        print("Die Summe lautet: ", summe)
        correct_input = True