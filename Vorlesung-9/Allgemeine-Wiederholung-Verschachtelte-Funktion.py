erste_zahl = 32
zweite_zahl = 16

def derersteschritt(a):
    return a + 15

def derzweiteschritt(b):
    return b * 1

ergebnis = derersteschritt(derzweiteschritt(erste_zahl/(4**2)))
print("Ergebnis:", ergebnis)

# Was kommt raus, wenn Sie folgenden Code ausführen?
# Ergebnis: 17