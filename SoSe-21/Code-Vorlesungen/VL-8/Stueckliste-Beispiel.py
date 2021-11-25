# Als Mitarbeiter/in im Operationsmanagement von SpaceX sind Sie damit beauftragt worden, eine entsprechende Stückliste
# für die Produktion des Antriebs für das nächste „Starship“ aufzusetzen. Aus einem Briefing haben Sie folgende Bestandteile mitnehmen
# können, die Sie nun in einer digitalen Liste pflegen sollen.
# • Primäre Hüllenverkleidung
# • Schubtriebwerke
# • Navigationstriebwerke
# • Hitzeschilde
# • Boardcomputer
# • Treibstoff

# Initialisieren der Stücklisten-Variable
stueckliste = []
# Initialisieren der Schleifen-Variable
weitere_eingabe = True

while weitere_eingabe:
    # Den Nutzer um eine Eingabe bitten
    bauteil = input("Bitte geben Sie das Bauteil ein: ")
    # Das Bauteil der Stückliste hinzufügen
    stueckliste.append(bauteil)
    entscheidung = input("Möchten Sie noch ein weiteres Bauteil erfassen (ja/nein)?")
    if entscheidung.upper() != "JA":
        weitere_eingabe = False

# Die Stückliste ausgeben
print(stueckliste)
