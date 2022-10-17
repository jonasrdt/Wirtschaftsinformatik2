

# while-Schleife läuft solange, wie die mit ihr verbundene Bedingung True ist
# while-Schleifen nutzen wir dann, wenn wir die Anzahl der Durchläufe NICHT kennen

zahl = 0
obergrenze = 10

while zahl < obergrenze:
    zahl = float(input("Bitte geben Sie irgendeine Zahl ein: "))
    if zahl < obergrenze:
        print("Die eingegeben Zahl lautet", zahl," und ist kleiner als 10.")
        print("Deshalb läuft die Schleife nochmal.")
    else:
        print("Es wurde eine Zahl größer als",obergrenze,"eingegeben. Die Zahl lautet: \t", zahl)
        