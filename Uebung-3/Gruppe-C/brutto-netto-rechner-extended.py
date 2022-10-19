# Definieren der 
korrekte_eingabe = False
while not korrekte_eingabe:
    familienstand = input("Bitte geben Sie Ihren Familienstand an: ")
    print("Der von Ihnen eingegeben Familienstand ist:", familienstand)
    if familienstand.lower() == "ledig":
        print("Sie haben angegeben, dass Sie ledig sind.")
        korrekte_eingabe = True
    elif familienstand.lower() == "verheiratet":
        print("Sie haben angegeben, dass Sie verheiratet sind.")
        korrekte_eingabe = True
    else:
        print("Sie scheinen weder verheiratet noch ledig zu sein. Überprüfen Sie Ihre Eingabe.")

bruttogehalt = int(input("Bitte geben Sie Ihr Bruttogehalt ein: "))
