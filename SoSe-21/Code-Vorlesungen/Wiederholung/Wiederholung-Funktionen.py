b = 5 # integer
c = 5.5 # float
d = True # boolean
e = [1, 2, 3] # liste
f = {'a': 2, 'b': 3} # Dictionary

def wertsteigerung(wert, prozente):
    wertgegenstand = wert # 195000
    prozentuales_wachstum = prozente # 0.04
    endwert = wertgegenstand * prozentuales_wachstum # 195000 * 0.04 = 7800
    return endwert

print(wertsteigerung(195_000, 0.04))


