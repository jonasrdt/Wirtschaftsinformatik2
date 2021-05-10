
# for - Schleife
# for - als Ansage, dass ab jetzt eine for-Schleife kommt
# zaehler - der zählt hoch, wie oft die Schleife schon gelaufen ist (häufig i o.ä.)
# in - gibt die Bedingung für die for-Schleife an
# range() - ist eine Funktion, mithilfe derer Sie bestimmte Schritte gehen und zählen können

# range(start, stop, step)
for spalten in range(15):
    for zeilen in range(15):
        print("*", end="")
    print()
