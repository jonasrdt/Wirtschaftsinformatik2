# Funktionsdefinition
def trenner():
    print("-----------------------------------")

def texteingabe(frage, antwort1, antwort2):
    gueltige_eingabe = False
    while not gueltige_eingabe:
        ergebnis = input(frage)
        if ergebnis.upper() == antwort1.upper() or ergebnis.upper() == antwort2.upper():
            trenner()
            print("Gute Wahl, du hast dich für", ergebnis, "entschieden.")
            trenner()
            gueltige_eingabe = True
        else:
            print("Bitte wähle entweder", antwort1,"oder", antwort2)
    return ergebnis

def spielerdefinition(nummer):
    print("Herzlich Willkommen Spieler", nummer)
    geschlecht = texteingabe("Bist du ein Abenteurer oder eine Abenteurerin: ", "Abenteurer", "Abenteurerin")
    if geschlecht.upper() == "ABENTEURER":
      print("Herzlich Willkommen Abenteurer")
    elif geschlecht.upper() == "ABENTEURERIN":
        print("Herzlich Willkommen Abenteurerin")

    name = input("Bitte teile mir deinen Namen mit: ")
    print("Sei Willkommen", name)
    trenner()
    waffe = texteingabe("Bitte wähle zwischen Schwert und Bogen: ", "Schwert", "Bogen")
    ruestung = texteingabe("Bitte wähle zwischen Lederwams und Kettenhemd: ", "Lederwams", "Kettenhemd")

spielerdefinition(1)
spielerdefinition(2)

print("Du stehst vor einem furchteinflössenden Gebäude. Auf dem Dach des Gebäudes befindet sich die leuchtende Schatztruhe mit der Klausurmusterlösung.")
betreten = texteingabe("Möchtest du das Gebäude betreten? ", "Ja", "Nein")

if betreten.upper() == "JA":
    print("Du betrittst das Gebäude durch einen Nebeneingang.")
    print("Dort triffst du auf einen Wärter, der deinen Ausweis kontrollieren will.")
if betreten.upper() == "NEIN":
    print("Du gehst nach Hause und hast wohl nicht das Zeug zum Abenteurer.")
trenner()

entscheidung_waerter = texteingabe("Zeigst du dem Wärter deinen Ausweis oder kämpfst du (Ausweis/Kampf)? ", "Ausweis", "Kampf")
if entscheidung_waerter.upper() == "KAMPF":
    print("Du ziehst dein/deinen", waffe, "der Kampf beginnt!")
elif entscheidung_waerter.upper() == "AUSWEIS":
    print("Er kontrolliert deinen Ausweis und lässt dich passieren.")