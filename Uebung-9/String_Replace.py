
satz = input("Bitte geben Sie einen Satz ein: ")
sonderzeichen_ohne_Leerzeichen = [".", ",", ":", "$", ";", "/", "'", "*", "+", "-", "%", "?", "!", "1", "2", "3"]
for zeichen in sonderzeichen_ohne_Leerzeichen:
    satz = satz.replace(zeichen, "")
print(satz)
anzahl_woerter = len(satz.split(" "))

satz = satz.replace(zeichen, "")    
print("Der Satz ist", len(satz), "Zeichen lang. Ohne Leerzeichen.")
print("Der Satz hat", anzahl_woerter, "Wörter.")
print("Die durchschnittliche Wortlänge beträgt:", len(satz) / anzahl_woerter)