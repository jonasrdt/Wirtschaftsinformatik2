# Erstellen Sie ein Python-Programm mit den folgenden Anforderungen:
# • Der Anwender soll dazu aufgefordert werden, sein monatliches Bruttogehalt einzugeben.
# • Liegt das Gehalt über 2.500 €, sind 22% Steuern zu zahlen, ansonsten 18%.
# • Innerhalb des Programms soll anhand des Gehalts entschieden werden, welcher Steuersatz zur Anwendung kommt.


bruttogehalt = float(input("Bitte geben Sie Ihr Bruttogehalt ein: "))
familienstand = input("Bitte geben Sie Ihren Familienstand ein: ")

if bruttogehalt >= 4000 and familienstand.lower() == "ledig":
      print("Es ergibt sich ein Steuerbetrag von:", bruttogehalt * 0.26, "€.")
elif bruttogehalt >= 4000 and familienstand.lower() == "verheiratet":
      print("Es ergibt sich ein Steuerbetrag von:", bruttogehalt * 0.22, "€.") 
elif 4000 > bruttogehalt >= 2500 and familienstand.lower() == "ledig":
    print("Es ergibt sich ein Steuerbetrag von:", bruttogehalt * 0.22, "€.")
elif 4000 > bruttogehalt >= 2500 and familienstand.lower() == "verheiratet":
    print("Es ergibt sich ein Steuerbetrag von:", bruttogehalt * 0.18, "€.")
else:
    print("Es konnte kein Steuersatz zugeordnet werden")