
# ETH = 0, ADA = 1, BTC = 2, LINK = 3, BTT = 4
# krypto = ["ETH", "ADA", "BTC", "LINK", "BTT"]

# Ausgangstext
text = "Die Kryptowährung Ethereum erreicht in diesem Jahr noch 10.000,00€ und ist eine tolle Kryptowährung."

# Splitten des Textes in einzelne Wörter in einer Liste
text_gesplittet = text.split(" ")
# print(text_gesplittet)

# Initiieren der Variable
anzahl_krypto = 0

# Zählen der Wörter in der Liste text_gesplittet
for wort in text_gesplittet:
    # print(wort)
    if wort.upper() == "KRYPTOWÄHRUNG" or wort.upper() == "KRYPTOWÄHRUNG.":
        anzahl_krypto += 1

# Berechnung des prozentualen Anteils des gesuchten Wortes 'Kryptowährung'
prozentualer_Anteil = round(anzahl_krypto/len(text_gesplittet) * 100, 2)

# Ausgabe der Inhalte
print("Das Wort 'Kryptowährung' ist:", anzahl_krypto, "Mal vorgekommen.")
print("Insgesamt gab es:", len(text_gesplittet), "Wörter.")
print("Das Wort 'Kryptowährung' hatte:", prozentualer_Anteil, "Prozent Anteil.")