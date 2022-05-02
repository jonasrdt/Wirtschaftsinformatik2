
####################
### Datentypen ####
####################

ganze_zahl = 5 # Integer
fliesskommazahl = 5.5 # Float
wahr = True # Boolean
liste = ["Jonas", 29, True, 0.43]
student = ["Felix", "Jürgens", 23, 45, "Elektrotechnik", "Kiel", "01.09.2021"] # Liste
student_2 = {"Name": "Felix",
             "Nachname": "Jürgens",
             "Alter": 23,
             "Studiengang:": "Elektrotechnik"} # Dictionary

####################
### Schleifen ####
####################

abbruchbedingung = False
while not abbruchbedingung:
    zahl = int(input("Bitte geben Sie eine Zahl ein: "))
    if zahl > 5:
        abbruchbedingung = True

for zaehler in range(1,10):
    print(zaehler)
 
