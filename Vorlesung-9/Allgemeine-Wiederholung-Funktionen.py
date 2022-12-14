# Definieren der globalen Variable 'mwst'
mwst = 0.19

# Definieren der Parameter 'betrag' und 'mwst' 
def mehrwertsteuer(betrag, mwst):
    # 'ergebnis' ist eine lokale Variable, 'betrag' ist ebenso eine lokale Variable
    ergebnis = betrag * (1 + mwst)
    # returnen der lokalen Variable 'ergebnis' in den globalen Kontext
    return ergebnis

# 'summe' ist eine globale Variable
summe = float(input("Bitte geben Sie einen Betrag ein: "))
# Ausführen der Funktion mehrwertsteuer()
print("Der Betrag inkl. MwSt. beträgt:", mehrwertsteuer(summe, mwst))