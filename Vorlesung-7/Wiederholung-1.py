fliesskommazahl = 2.45                              # float
string = "Das ist eine Zeichenkette"                # string
ganze_zahl = 10                                     # int
wahroderfalsch = True                               # boolean
dictionary = {"Name": "Jonas",                      # dictionary
              "Schniefnase": True}
einkaufsliste = ["Brot", "Genussscheiben", "Bier"]  # Liste


alter = int(input("Bitte geben Sie Ihr Alter ein: "))
if alter < 18:
    print("Du darfst noch keine Zigaretten kaufen.")
    
# Modulo
ergebnis = ganze_zahl % fliesskommazahl
print(ergebnis)