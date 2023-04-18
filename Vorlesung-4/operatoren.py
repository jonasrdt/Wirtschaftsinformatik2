
# text = "wabadu"
# print(2*text)

# Teilen mit Rest mit Modulo

zahl = int(input("Bitte geben Sie eine Zahl ein: "))
zahl_modulo = zahl % 2

if zahl_modulo == 0: 
    print("Die eingebene Zahl", zahl, "ist gerade.")
else:
    print("Die eingegebene Zahl", zahl, "ist ungerade.")