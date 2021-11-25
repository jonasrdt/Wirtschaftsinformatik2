# a = 15 # integer
# b = 15.5 # float
# c = True # Boolean
# d = "Das hier ist ein Satz" # String
# #Index 0     1     2        3        4
# e = ["Das", "ist", "eine", "Liste", ["Verschachtelung", "yeah"]] # Liste
# f = {"Jonas": 2101357,
#      "Peter": 2101356} # Dictionary


# Bitte schreiben Sie ein Programm in Python, was das Alter des Nutzers nach Eingabe
# überprüft. Der Nutzer muss mindestens 18 Jahre alt sein. Achten Sie hierbei
# auf Ausnahmebehandlungen.

# Typumwandlung des "str" inputs in einen "int", damit wir vergleichen können
schleifeläuft = True
while schleifeläuft: # not False = True
    # try, except prüft nur auf technische Fehler
    try:
        alter = int(input("Bitte geben Sie Ihr Alter ein: "))
        # Inhaltliche Prüfung mithilfe von if,else
        if alter >= 18:
            print("Sie dürfen die Seite besuchen.")
            schleifeläuft = False
        else:
            print("Leider sind Sie nicht alt genug um die Seite zu besuchen.")
    except:
        print("Bitte geben Sie nur ganze Zahlen ein.")