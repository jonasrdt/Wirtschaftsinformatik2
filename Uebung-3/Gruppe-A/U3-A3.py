# Erstellen Sie ein Python-Programm mit den folgenden Anforderungen:
# • Der Anwender soll dazu aufgefordert werden, sein monatliches Bruttogehalt
# einzugeben.
# • WENN das Gehalt über 2.500 € liegt, DANN sind 22% Steuern zu zahlen, ANSONSTEN 18%.
# • Innerhalb des Programms soll anhand des Gehalts entschieden werden, welcher
# Steuersatz zur Anwendung kommt.

# Definition von Variablen
hoechststeuersatz = 0.22
niedrigersteuersatz = 0.18

# Den Nutzer auffordern, sein Bruttogehalt einzugeben und den Datentypen auf Float ändern
bruttogehalt = float(input("Bitte geben Sie Ihr Bruttogehalt ein: "))
print("Sie haben ein Bruttogehalt i.H.v.", bruttogehalt, "€ eingegeben.")

# Wenn das Bruttogehalt unter dem Einkommenssteuerfreibetrag liegt …
if 0 < bruttogehalt < 832:
    print("Ihr Einkommen liegt unter dem Einkommenssteuerfreibetrag i.H.v. 9.984,00 €. Es fallen keine Steuern an.")
# Wenn das Bruttogehalt über 2.500,00€ liegt
elif bruttogehalt > 2_500:
    #… führe nachfolgendes aus:
    print("Bei Ihrem Bruttogehalt i.H.v.", bruttogehalt, "€ fallen", hoechststeuersatz * 100,"%  Steuern an.")
    print("Es ergibt sich eine Steuerlast i.H.v.", bruttogehalt * hoechststeuersatz)
elif 0 < bruttogehalt <= 2_500:
    #… andernfalls führe dies hier aus:
    print("Bei Ihrem Bruttogehalt i.H.v.", bruttogehalt, "€ fallen", niedrigersteuersatz * 100,"% Steuern an.")
    print("Es ergibt sich eine Steuerlast i.H.v.", bruttogehalt * niedrigersteuersatz)
else:
    #… falls der Nutzer negative Zahlen eingegeben hat.
    print("Bitte geben Sie nur positive Zahlen ein.")


