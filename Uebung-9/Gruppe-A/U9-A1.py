# Schreiben Sie ein Python-Programm, welches ein beliebiges Wort in
# das DIN 5009-Alphabet überführt. Z. B. könnte der Programmablauf so aussehen:

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
zahlen = ["0","1","2","3","4","5","6","7","8", "9"]

wort = input("Bitte geben Sie ein Wort ein: ").upper()

# This code is iterating over each character in the input word and checking if it is a number. If the
# character is a number, it prints a message saying that it is a number and replaces the number with
# an empty string in the input word. This is done to remove any numbers from the input word before
# converting it to the DIN 5009 alphabet.
for buchstabe in wort:
    if buchstabe in zahlen:
        print(buchstabe, "ist eine Zahl. Erwischt!")
        wort = wort.replace(buchstabe, "")

# This code is iterating over each character in the input word and checking if it exists in the DIN
# 5009 alphabet dictionary. If the character exists in the dictionary, it prints the character and its
# corresponding word in the DIN 5009 alphabet.
for buchstabe in wort:
    if buchstabe in din_alphabet:
        print(buchstabe, "\t", din_alphabet[buchstabe])

