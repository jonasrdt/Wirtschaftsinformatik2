# Erstellen Sie ein Python-Programm mit den folgenden Anforderungen:
# • Der Anwender soll dazu aufgefordert werden, sein monatliches Bruttogehalt
# einzugeben.
# • WENN das Gehalt über 2.500 € liegt, DANN sind 22% Steuern zu zahlen, ANSONSTEN 18%.
# • Innerhalb des Programms soll anhand des Gehalts entschieden werden, welcher
# Steuersatz zur Anwendung kommt.

# Definition von Variablen
hoechststeuersatz = 0.26
mittlerersteuersatz = 0.22
niedrigersteuersatz = 0.18

# Den Nutzer auffordern, sein Bruttogehalt einzugeben und den Datentypen auf Float ändern
bruttogehalt = float(input("Bitte geben Sie Ihr Bruttogehalt ein: "))
print("Sie haben ein Bruttogehalt i.H.v.", bruttogehalt, "€ eingegeben.")

# Den Nutzer auffordern, seinen Familienstand einnzugeben und 
familienstand = input("Bitte geben Sie Ihren Familienstand an (ledig/verheiratet): ")
print("Sie haben den Familienstand", familienstand, "angegeben.")

if bruttogehalt > 4000 and familienstand.lower() == "ledig":
    print("Es fallen Steuern i.H.v.", bruttogehalt * hoechststeuersatz, "an.")
elif bruttogehalt > 4000 and familienstand.lower() == "verheiratet":
    print("Es fallen Steuern i.H.v.", bruttogehalt * mittlerersteuersatz, "an.")
elif 0 < bruttogehalt <= 4000 and familienstand.lower() == "ledig":
    print("Es fallen Steuern i.H.v.", bruttogehalt * mittlerersteuersatz, "an.")
elif 0 < bruttogehalt <= 4000 and familienstand.lower() == "verheiratet":
    print("Es fallen Steuern i.H.v.", bruttogehalt * niedrigersteuersatz, "an.")
else:
    print("Bitte geben Sie nur positive Zahlen ein.")