zahl = int(input("Bitte geben Sie eine natürliche Zahl größer 0 ein: "))
summe = 1

for i in range(1, zahl+1):
    summe = summe * i
    
print(f"Die Fakultaet ist {summe}")