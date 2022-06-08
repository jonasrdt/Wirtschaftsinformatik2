# range(start, stop, step)
for anzahl in range(1, 100, 5):
    print(anzahl)

richtige_eingabe = False
while not richtige_eingabe:
    try:
        alter = int(input("Bitte geben Sie Ihr Alter ein: "))
        richtige_eingabe = True
    except:
        print("Bitte geben Sie nur eine gültige Zahl ein.")