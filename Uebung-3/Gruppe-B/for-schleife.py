

# Lachs-Quiche Rezept
# Hierfür müssen 750g Porree geschnitten werden
# Eine Porree Stange hat 250g


anzahl_porree = int(input("Bitte geben Sie die Anzahl an Porreestangen ein: "))

# range(start, stop, step)
# Wenn kein step definiert ist, wird immer 1 Schritt gemacht
for porreestange in range(1, anzahl_porree+1):
    print("Ich habe insgesamt", porreestange,"Porreestangen geschnitten")
    print("ʕ •ᴥ•ʔ")
print("Ich bin jetzt fertig und habe", anzahl_porree, "Porreestangen geschnitten.")