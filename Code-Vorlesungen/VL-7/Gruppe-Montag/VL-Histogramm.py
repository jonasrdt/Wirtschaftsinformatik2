
# Menge an Werten
zahlen = "1203456708948673516874354531568764645"


# Initialisieren der Histogramm Variable
histogramm = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]

for index in range(len(zahlen)):
    histogramm[int(zahlen[index])] += 1

for i in range(0,10):
    print("Die Zahl", i, "kommt", histogramm[i], "Mal vor.")