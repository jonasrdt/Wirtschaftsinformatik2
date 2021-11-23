din_alphabet = {
    "A":	"Anton",
    "Ä":	"Ärger",
    "B":	"Berta",
    "C":	"Cäsar",
    "D":	"Dora",
    "E":	"Emil",
    "F":	"Friedrich",
    "G":	"Gustav",
    "H":	"Heinrich",
    "I":	"Ida",
    "J":	"Julius",
    "K":	"Kaufmann",
    "L":	"Ludwig",
    "M":	"Martha",
    "N":	"Nordpol",
    "O":	"Otto",
    "Ö":	"Ökonom",
    "P":	"Paula",
    "Q":	"Quelle",
    "R":    "Richard",
    "S":	"Samuel",
    "ẞ":	"Eszett",
    "T":	"Theodor",
    "U":	"Ulrich",
    "Ü":	"Übermut",
    "V":	"Viktor",
    "W":	"Wilhelm",
    "X":	"Xanthippe",
    "Y":	"Ypsilon",
    "Z":	"Zacharias"
}

wort = input("Bitte geben Sie ein Wort ein: ")
for buchstabe in wort:
    gb = buchstabe.upper()
    if gb in din_alphabet:
        print(gb + "\t" + din_alphabet[gb])
    else:
        print(gb + "\t" + gb)
