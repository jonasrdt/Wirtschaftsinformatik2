for i in range(900000,1000000, 1):
    a = i % 5
    if a > 4:
        print("Fehler bei:", i)
        print("Mit Modulo:", a)