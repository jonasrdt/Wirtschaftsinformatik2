# Schreiben Sie ein Programm, mithilfe dessen eine Pizza bestellt
# deren Menge eingegeben und der Gesamtpreis berechnet werden kann.
# Die Pizza kostet im Mittagsangebot immer 7,00€

# Definieren der Variable Mittagsangebotspreis
mittagsangebotspreis = 7

menge = int(input("Bitte geben Sie die Menge der zu bestellenden Pizza ein: "))
if menge > 0:
    gesamtsumme= round(menge * mittagsangebotspreis, 2)
    print("Du hast:", menge, "Pizzen bestellt. Das kostet dich:", gesamtsumme, "€.")
else:
    print("Du hast null oder eine negative Zahl eingegeben. Schade.")

