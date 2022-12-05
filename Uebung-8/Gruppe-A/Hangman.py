
def trenner(anzahl):
    for i in range(anzahl):
        print("-", end= " ")
    print()

# Zu erratenes Wort
wort = "Sprite"
leben = 5

# Das gesuchte Wort hat 6 Buchstaben
# Wort: _ _ _ _ _ _ 
# Wort: _ _ _ _ _ e 
# Wort: S _ _ _ _ e 
# Wort: S p _ _ _ e 


trenner(15)
print("Willkommen beim Hangman-Spiel")
print("Das von Ihnen zu erratene Wort hat:", len(wort), "Zeichen.")
trenner(15)
erraten = False
while not erraten:
    buchstabe = input("Bitte geben Sie ein Zeichen ein: ")
    if buchstabe in wort:
        print("Mach was")
    else:
        trenner(15)
        print("Der Buchstabe",buchstabe,"kam leider nicht in dem Wort vor.")
        leben -= 1
        print("Du verlierst ein Leben. Du hast nur noch", leben, "Leben.")
        if leben == 0:
            print("Du hast leider verloren. Das Wort wäre", wort, "gewesen.")
            break
        trenner(15)