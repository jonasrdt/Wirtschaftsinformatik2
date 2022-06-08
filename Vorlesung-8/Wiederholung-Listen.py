                # 0      # 1      # 2
einkaufsliste = ["Cola", "Chips", "Bier"]

print("Die Einkaufsliste hat", len(einkaufsliste) ,"Elemente.")

for eintrag in einkaufsliste:
    print(eintrag)

einkaufsliste.append("Cracker")
print(einkaufsliste)
einkaufsliste.insert(2, "Fanta")
print(einkaufsliste)

            # 0
staedte = [["Paris", 3.18, "FR"],
            # 1
           ["Berlin", 3.18, "DE"],
            # 2
           ["Verbania", 0.03, ["IT", "Verbano-Cusio-Ossola"]]]

print(staedte[2][2][1])
# Gibt Verbano-Cusio-Ossola aus