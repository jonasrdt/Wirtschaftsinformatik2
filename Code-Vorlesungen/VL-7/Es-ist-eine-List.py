
# ETH = 0, ADA = 1, BTC = 2, LINK = 3, BTT = 4
# krypto = ["ETH", "ADA", "BTC", "LINK", "BTT"]

# krypto.append("LTC")
# krypto.append("DOGE")

# print(krypto[0])


# text = "Die Kryptowährung Ethereum erreicht in diesem Jahr noch 10.000,00€ und ist eine tolle Kryptowährung ."

# text_gesplittet = text.split(" ")

# anzahl_krypto = 0
# for wort in text_gesplittet:
#     # print(wort)
#     if wort == "Kryptowährung":
#         anzahl_krypto += 1

# print("Insgesamt gab es:", len(text_gesplittet), "Wörter.")
# print("Das Wort 'Kryptowährung' ist:", anzahl_krypto, "Mal vorgekommen.")


zahlen = "54684354359212900596484687465468043501201"

histogramm = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]

for index in range(len(zahlen)):
    histogramm[int(zahlen[index])] += 1

for i in range(0, 10):
    print("Die Zahl", i, "kommt", histogramm[i], "mal vor.")