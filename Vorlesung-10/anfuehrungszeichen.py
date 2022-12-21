

# Sie können sowohl die englischen Anführungszeichen => ' '
# als auch die deutschen Anführungszeichen => " "
# benutzen, müssen sich aber innerhalb eines Statements
# auf eine committen. Bspw.: print(' bla bla  ')
# oder aber print(" bla bla ")
# in der Mischung wäre folgendes denkbar: print('Jetzt Zitat: "Nerd today, boss tomorrow" ')

tante_emma_laden = {
    "brot": 5,
    "wasser": 10,
    "tee": 2
}

for ware in tante_emma_laden.keys():
    print("Im Tante Emma Laden befindet sich:", ware)