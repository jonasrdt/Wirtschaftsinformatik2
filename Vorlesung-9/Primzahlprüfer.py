# Schreiben Sie ein Programm welches prüft,
# ob die eingegebene Zahl eine Primzahl ist oder nicht.
# Achten Sie auf Fehleingaben durch den User etc. pp.

# Eine Zahl ist dann eine Primzahl, wenn Sie nur
# durch sich selbst und eins glatt teilbar ist.

zahl = int(input("Bitte geben Sie eine Zahl ein: "))
# Eingabe: 13
if 0 <= zahl < 2:
    print(zahl, "ist keine Primzahl")
else:
    for zaehler in range(2, int(zahl**0.5)+1):
        if zahl % zaehler == 0:
            print(zahl, "ist keine Primzahl")
            break
        else:
            print(zahl, "ist eine Primzahl.")