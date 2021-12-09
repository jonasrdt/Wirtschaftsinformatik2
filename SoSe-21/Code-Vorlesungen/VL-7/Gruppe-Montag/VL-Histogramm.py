# import matplotlib.pyplot as plt

# Menge an Werten
zahlen = "1203456708948673516874354531568764645"

# Initialisieren der Histogramm Variable
histogramm = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]

for index in range(len(zahlen)):
    histogramm[int(zahlen[index])] += 1

# plt.hist(histogramm, bins = 9)
# plt.show()

for i in range(0,10):
    print("Die Zahl", i, "kommt", histogramm[i], "Mal vor.")