

# Definieren einer Zähl-Variable mit dem Wert 9
zaehl_variable = 9

for zeilen in range(1, zaehl_variable+1):
    # Einfügen der Leerzeichen
    for leerzeichen in range(zaehl_variable-zeilen+1):
        print(" ", end =" ")
    # Hochzählen der Werte
    for werte in range(1, zeilen+1):
        print(werte, end= " ")
    # Runterzählen der Werte
    for werte in range(zeilen-1, 0, -1):
        print(werte, end = " ")
    print()
