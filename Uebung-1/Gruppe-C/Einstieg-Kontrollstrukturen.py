# Wenn der Wert des Warenkorbs 50.00 € übersteigt,
# fallen die Versandkosten weg.

# Wert des Warenkorbs in Euro
warenkorb_wert = 55

# Wenn der Wert des Warenkorbs kleiner 50 und größer 30 ist...
if 50 >= warenkorb_wert >= 30:
    # ... setze die Versandkosten auf 3.00 €
    versandkosten = 3
elif 30 > warenkorb_wert >= 0.1:
    # ... setze die Versandkosten auf 4.95 €
    versandkosten = 4.95
# Andernfalls...
else:
    # ... setze die Versandkosten auf 0 €
    versandkosten = 0
    
# Berechnung der Gesamtkosten auf Basis der Variablen warenkorb_wert und versandkosten
gesamtkosten = warenkorb_wert + versandkosten

print("Für den Wert des Warenkorbs i.H.v.", warenkorb_wert, "€, fallen", versandkosten, "€ Versandkosten an.")
print("Ihre Gesamtkosten belaufen sich auf: ", gesamtkosten)