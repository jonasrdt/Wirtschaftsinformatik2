
# Variablendefinition
mwst = 0.19

# Eingabe des Preises durch den Nutzer
netto = float(input("Bitte geben Sie einen Nettobetrag ein: "))

steuerbetrag = netto * mwst
print("Der Steuerbetrag beträgt: ", steuerbetrag)

brutto = steuerbetrag + netto
print("Der Bruttopreis beträgt: ", brutto)