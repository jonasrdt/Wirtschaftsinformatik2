
zahl = int(input("Bitte geben Sie eine Zahl ein:"))

if zahl > 10:
    print ("Die Zahl", zahl, "ist größer als 10.")
    if zahl <= 100:
        print ("Die Zahl", zahl, "ist jedoch kleiner als 100.")
    else:
        print ("Die Zahl ist größer als 100.")

elif zahl < 10:
    print ("Die Zahl", zahl, "ist kleiner als 10.")

else:
    print ("Die Zahl", zahl, "ist gleich 10.")