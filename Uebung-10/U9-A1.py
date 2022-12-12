# Schreiben Sie ein Python-Programm, welches ein beliebiges Wort in das DIN 5009-Alphabet überführt.

din_alphabet = {
    "A":    "Anton",
    "Ä":    "Ärger",
    "B":    "Berta",
    "C":    "Cäsar",
    "D":    "Dora",
    "E":    "Emil",
    "F":    "Friedrich",
    "G":    "Gustav",
    "H":    "Heinrich",
    "I":    "Ida",
    "J":    "Julius",
    "K":    "Kaufmann",
    "L":    "Ludwig",
    "M":    "Martha",
    "N":    "Nordpol",
    "O":    "Otto",
    "Ö":    "Ökonom",
    "P":    "Paula",
    "Q":    "Quelle",
    "R":    "Richard",
    "S":    "Samuel",
    "ẞ":    "Eszett",
    "T":    "Theodor",
    "U":    "Ulrich",
    "Ü":    "Übermut",
    "V":    "Viktor",
    "W":    "Wilhelm",
    "X":    "Xanthippe",
    "Y":    "Ypsilon",
    "Z":    "Zacharias"
}

# Eine Liste mit allen Dezimalzahlen als Integer-Werte
zahlen = [1,2,3,4,5,6,7,8,9,0]
nutzereingabe = input("Bitte geben Sie ein beliebiges Wort ein: ")
zahl_in_nutzereingabe = False
while not zahl_in_nutzereingabe:
    for zahl in zahlen:
        # Temporäres Ändern des Zählers zahl in einen String zwecks Vergleich
        if str(zahl) in nutzereingabe:
            print("Bitte geben Sie ausschließlich Buchstaben ein, keine Zahlen.")
        else:
            zahl_in_nutzereingabe = True

# Iterating through the user input and checking if the character is in the dictionary. If it is, it
# prints the character and the value of the dictionary. If it is not, it prints the character and the
# string "unbekanntes Zeichen".
for zeichen in nutzereingabe:
    if zeichen.upper() in din_alphabet:
        print(zeichen.upper(), "\t", din_alphabet[zeichen.upper()])
    else:
        print(zeichen.upper(), "\t", "unbekanntes Zeichen")