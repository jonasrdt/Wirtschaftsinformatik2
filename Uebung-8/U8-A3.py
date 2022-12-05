warenlager = {  'Butter': 1.90,
                'Brot': 2.30,
                'Schokolade': 1.50,
                'Apfel': 1.20
             }

def zahleneingabe(datentyp):
    korrekte_eingabe = False
    while not korrekte_eingabe:
        try:
            zahl = datentyp(input("Bitte geben Sie die Zahl ein: "))
            korrekte_eingabe = True
        except:
            print("Bitte geben Sie nur Zahlen ein.")
    return zahl

# Hauptprogramm
im_warenlager = False
while not im_warenlager:
    ware = input("Bitte geben Sie die Ware ein, die Sie kaufen möchten: ")
    if ware in warenlager:
        menge = zahleneingabe(int)
        print("Sie wollen", menge, ware, "kaufen.")
        kosten = warenlager[ware] * menge
        print("Hierfür entstehen Ihnen Kosten i.H.v.", kosten, "€.")
    else:
        print(ware, "befindet sich nicht im Warenlager. Bitte wählen Sie etwas anderes.")
    