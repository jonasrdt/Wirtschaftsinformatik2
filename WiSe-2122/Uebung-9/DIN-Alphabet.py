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
    "ß":    "Eszett",
    "T":    "Theodor",
    "U":    "Ulrich",
    "Ü":    "Übermut",
    "V":    "Viktor",
    "W":    "Wilhelm",
    "X":    "Xanthippe",
    "Y":    "Ypsilon",
    "Z":    "Zacharias"
}

wort = input("Bitte geben Sie ein beliebiges Wort ein: ")

for char in wort:
    if char != " ":
        if char.upper() in din_alphabet:
            print(char, "\t", din_alphabet[char.upper()])
    elif char == " ":
        print()
    else:
        print("Diesen Buchstaben gibt es nicht im Alphabet")