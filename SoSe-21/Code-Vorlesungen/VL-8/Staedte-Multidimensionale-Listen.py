# In diesem Städte-Beispiel sollen mehrdimensionale Listen gezeigt werden

# Eindimensionale Liste
# eindimensionale_liste = ["Berlin", 4_000_000]
# print(eindimensionale_liste)

mehrdimensionale_liste = [["Berlin", "DE", 4_000_000],
                          ["Rom", "IT", 2_800_000],
                          ["Madrid", "ESP", 6_600_000],
                          ["New York", "USA", 8_400_000]]

stadt = ""
max_einwohner = 0

for zeile in mehrdimensionale_liste:
    if zeile[2] > max_einwohner:
        stadt = zeile[0]
        max_einwohner = zeile[2]

print(stadt, "hat die meisten Einwohner mit:", max_einwohner, "Einwohnern.")