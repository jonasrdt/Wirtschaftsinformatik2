
def trenner(anzahl):
    for i in range(anzahl):
        print("-", end= " ")
    print()
    
def worthuelse(wort):
    worthuelse = []
    for buchstabe in wort:
        worthuelse.append("_")
    return worthuelse

# Zu erratenes Wort
wort = "Ananas"
wort_split = []
for el in wort:
    wort_split.append(el.lower())

worthuelse = worthuelse(wort)
leben = 5

trenner(15)
print("Willkommen beim Hangman-Spiel")
print("Das von Ihnen zu erratene Wort hat:", len(wort), "Zeichen:", worthuelse)
trenner(15)
erraten = False
while not erraten:
    buchstabe = input("Bitte geben Sie ein Zeichen ein: ")
    if buchstabe.lower() in wort.lower():
        for buchstabe_wort in wort_split:
            if buchstabe_wort.lower() == buchstabe.lower():
                stelle_buchstabe = wort_split.index(buchstabe.lower())
                worthuelse.insert(stelle_buchstabe, buchstabe)
                worthuelse.pop(stelle_buchstabe+1)
                print("Wort:", worthuelse)
                loesung = "".join(worthuelse)
                if loesung.lower() == wort.lower():
                    print("Juhu. Sie haben das Wort", wort, "richtig erraten.")
                    break
    else:
        trenner(15)
        print("Der Buchstabe",buchstabe,"kam leider nicht in dem Wort vor.")
        leben -= 1
        print("Du verlierst ein Leben. Du hast nur noch", leben, "Leben.")
        if leben == 0:
            print("Du hast leider verloren. Das Wort wäre", wort, "gewesen.")
            break
        trenner(15)