
# Passen Sie den Code so um eine Dictionary Abfrage an, dass der Gesamtpreis
# für die Bestellung von 5 Stücken Butter berechnet wird

warenlager = {  'Butter': 1.90,
                'Brot': 2.30,
                'Schokolade': 1.50,
                'Apfel': 1.20
             }

def preisberechnung():
    menge = 5
    return warenlager["Butter"] * menge