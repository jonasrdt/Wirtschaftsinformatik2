

satz = "Der Hund läuft in die Küche."
print("Der Satz hat", len(satz), "Zeichen.")
neuelaenge = len(satz) - 5
print("Der neue Satz wird", neuelaenge, "Zeichen haben.")
satz = satz[:neuelaenge]
print(satz)