stückliste = ["Primäre Hüllenverkleidung","Schubtriebwerke","Navigationstriebwerke","Hitzeschilde","Boardcomputer","Treibstoff"]
liste = []
abfrage = True
while abfrage:
    eingabe = input("Welches Bestandteil suchen Sie? ")
    if eingabe in stückliste:
        print("Bestandteil ist in der Stückliste enthalten.")
        liste.append(eingabe)
    else:
        print("Bestandteil ist nicht in der Stückliste enthalten.")
    
    korrekte_eingabe = False
    while not korrekte_eingabe:
        nochmal = input("Wollen Sie nochmal suchen? (Ja oder Nein eingeben) ")
        if nochmal.lower() == "ja":
            abfrage = True
            korrekte_eingabe = True
        elif nochmal.lower() == "nein":
            abfrage = False
            korrekte_eingabe = True
        else:
            print("Bitte geben Sie nur Ja/Nein ein.")

print(end="\n")
print("Fertige Stückliste:")
for element in liste:
    print("-", element)