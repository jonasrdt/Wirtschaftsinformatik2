

# Dictionary: Mehrere Werte mit mehreren Datentypen halten
telefonbuch = [["Jonas", "012784539"],        # Index 0
         ["Annika", "012784539"],       # Index 1
         ["Fabian", "012784539"],       # Index 2
         ["Nadine", "012784539"],       # Index 3
         ["Tamara", "012784539"],       # Index 4
         ["Tim", "012784539"],          # Index 5
         ["Jesper", "012784539"],       # Index 6
         ["Jannis", "012784539"]]       # Index 7

# Schreiben Sie ein Python Programm, welches den Nutzer bittet
# einen Namen einzugeben und daraufhin die Telefonnummer der Person ausgibt.

name = input("Bitte geben Sie den Namen ein, dessen Telefonnummer Sie erfahren wollen: ")

for eintrag in telefonbuch:
    if name == eintrag[0]: 
        print("Die Telefonnummer von", eintrag[0], "lautet:", eintrag[1])
        break # break, damit die Schleife abbricht, sobald der Eintrag gefunden wurde
# PROBLEM: Durchsuchen von Listen entspricht einer Komplexität O(n)