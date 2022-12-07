
gesamtpreis = 0
warenlager = {  'Butter': 1.90,
                'Brot': 2.30,
                'Schokolade': 1.50,
                'Apfel': 1.20
             }

print("Im Warenlager befinden sich folgende Waren:")
for ware in warenlager.keys():
    print("-", ware)

korrekte_ware = False
while not korrekte_ware:
    ware = input("Bitte geben Sie an, welche Ware Sie haben wollen: ")
    if ware in warenlager:
        korrekte_ware = True
        korrekte_menge = False
        while not korrekte_menge:
            try:
                menge = int(input("Bitte geben Sie die Menge ein, die Sie kaufen wollen: "))
                korrekte_menge = True
            except:
                print("Bitte geben Sie nur Zahlen ein.")
        print("Für", menge, ware, "entstehen Ihnen Kosten i.H.v.", warenlager[ware] * menge, "€.")
        gesamtpreis = gesamtpreis + warenlager[ware] * menge
        print("Die Summe Ihres aktuellen Warenkorbs beträgt:", gesamtpreis, "€.")
        entscheidung = input("Wollen Sie noch etwas kaufen (ja/nein): ")
        if entscheidung.lower() == "ja":
            korrekte_ware = False
    else:
        print("Bitte geben Sie nur Dinge an, die sich auch im Lager befinden.")


