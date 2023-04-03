# Schreiben Sie ein Programm, mithilfe dessen eine Pizza bestellt
# deren Menge angegeben und der Gesamtpreis berechnet werden kann.
# Die Pizza kostet im Mittagsangebot immer 7,00€

# Könnte so aussehen:
# Wie viele Pizzen möchtest du bestellen: 5
# In Ordnung. Du möchtest 5 Pizzen bestellen.
# Das kostet dich in Summe 35.00€.

mittagsangebot = 7
anzahl = float(input("Wie viele Pizzen möchtest du bestellen: "))
preis = round(anzahl * mittagsangebot, 2)
print("Du hast", anzahl, "Pizzen bestellt. Das kostet dich", preis, "Euro.")