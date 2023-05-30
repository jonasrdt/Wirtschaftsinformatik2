# satz = satz.replace(".", "")
# print(satz)
# satz = satz.replace(",", "")
# print(satz)
# satz = satz.replace(" ", "")
# print(satz)

satz = "Manche Leuchten, wenn man sie liest."
print(satz)
sonderzeichen = [" ", ".", ",", "!", "?", "§", "$", "%", "&", "/", "(", ")", "="]
for element in sonderzeichen:
    satz = satz.replace(element, "")
print(satz)

