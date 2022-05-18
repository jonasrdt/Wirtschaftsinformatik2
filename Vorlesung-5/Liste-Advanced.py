
# Leere Liste
woerter = []

# Bedeutungsvoller Satz
satz = input("Bitte geben Sie einen Satz ein: ")
woerter = satz.split(" ")
print("Der Satz ist", len(satz), "Zeichen lang und enthält", len(woerter), "Wörter.")
satz_bereinigt = satz.replace(" ", "").replace(".", "").replace(",", "").replace("'", "")
print(satz_bereinigt)
print("Die neue Satzlänge ist:", len(satz_bereinigt))
print("Durchschnittswortlänge:", round(len(satz_bereinigt)/len(woerter),2))
