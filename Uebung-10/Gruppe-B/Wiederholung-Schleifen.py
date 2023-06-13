

####################################################################
#### for-Schleife => Wenn die Anzahl der Durchläufe bekannt ist ####
####################################################################
# for-Schleife die von 1 bis einschließlich 4 zählt und
# den 'zaehler' innerhalb der Schleife ausgibt
# range (start, stop, step) => Wenn kein Step angegeben, dann immer Einerschritte
for zaehler in range(1,5):
    print(zaehler)
    
# for-Schleife die in 10er Schritten von 1 bis
# einschließlich 99 zählt und
# den 'zaehler' innerhalb der Schleife ausgibt
for zaehler_2 in range(1,99, 10):
    print(zaehler_2)

# for-Schleife die insgesamt fünf Mal durchzählt
# jedoch bei 0 startet, da kein anderer Start angegeben ist
for zaehler_3 in range(5):
    print(zaehler_3)

########################################################################
## while-Schleife => Wenn die Anzahl der Durchläufe nicht bekannt ist ##
########################################################################


# Die while-Schleife läuft solange, bis ein anderes
# Wort als 'go' eingegeben wird.
wort = "go"
while wort == "go":
    wort = input("Bitte geben Sie ein Wort ein:")
    print("Das eingegeben Wort lautet:", wort)
print("Die Schleife wurde beendet.")

# Die while-Schleife läuft solange, wie die mit ihr
# verknüpfte Bedingung WAHR (True) ist.
korrekte_eingabe = False
while not korrekte_eingabe:
    try:
        alter = int(input("Bitte geben Sie Ihr Alter ein: "))
        # Setzen der "Abbruchbedingung". Wenn "korrekte_eingabe" auf True gesetzt wird
        # ist in der mit der while-Schleife verknüpften Bedingung 
        # "not True" gesetzt => False, deshalb bricht die Schleife ab
        korrekte_eingabe = True
    except:
        print("Bitte geben Sie nur Zahlen ein.")
