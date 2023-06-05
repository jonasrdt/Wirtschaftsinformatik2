

sonderzeichen = [',', '.', '"', '!', '?', ':', '-', '#', '%', '&', '/', ' ', '0', '1']
satz = "Der#Hund!läuft.in-die Küche."

for element in sonderzeichen:
    satz = satz.replace(element, "")

print(satz)
