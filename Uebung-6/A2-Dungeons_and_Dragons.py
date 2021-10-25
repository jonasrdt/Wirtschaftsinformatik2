# Im folgenden soll ein Programm geschrieben werden, welches ein kleines Adventure darstellt

# Funktionsdefinition
def trenner():
    print("--------------------------------------------------------")

def texteingabe(frage, antwort1, antwort2):
    falsche_eingabe = True
    while falsche_eingabe:
        eingabe = input(frage)
        if eingabe.upper() == antwort1.upper() or eingabe.upper() == antwort2.upper():
            trenner()
            print("Gute Entscheidung. Du hast dich für", eingabe,"entschieden.")
            trenner()
            falsche_eingabe = False
        else:
            print("Bitte gib entweder", antwort1, "oder", antwort2, "ein.")
    return eingabe

# # # Hauptprogramm # # # # 
# # # # # # # # # # # # # # 
# Frage nach dem Geschlecht des Spielers
geschlecht = texteingabe("Bist du ein Abenteurer oder eine Abenteurerin: ", "Abenteurer", "Abenteurerin")
# Frage nach der Waffe
waffe = texteingabe("Du hast die Wahl zwischen einem Schwert oder einem Bogen: ", "Schwert", "Bogen")
# Frage nach der Rüstung
ruestung = texteingabe("Du hast die Wahl zwischen einem Lederwams oder einem Kettenhemd: ", "Lederwams", "Kettenhemd")
print("Du bist gut ausgerüstet, um nun dein Abenteuer zu starten.")
trenner()

print("Du stehst vor einem furchteinflössenden Gebäude. Auf dem Dach des Gebäudes steht eine leuchtende Kiste (Musterlösung für die Klausuren).")
betreten = texteingabe("Möchtest du das Gebäude betreten (ja/nein): ", "ja", "nein")

if betreten.upper() == "JA":
    print("Du betrittst das Gebäude durch einen der Seiteneingänge, als dich plötzlich ein Wärter nach deinem Ausweis fragt.")
    print("Zeigst du deinen Ausweis oder ziehst du dein/deine/deinen", waffe)
    kampfansage = input()
elif betreten.upper() == "NEIN":
    print("Du bist offensichtlich doch nicht für das Abenteuer gemacht. Geh nach Hause und übe noch etwas.")

if kampfansage.upper() == waffe.upper():
    trenner()
    print("Du ziehst dein/deine/deinen", waffe, "und machst dich bereit.")
    print("Der Wärter zieht ebenfalls seine Waffe und der Kampf beginnt.")
elif kampfansage.upper() == "AUSWEIS":
    trenner()
    print("Du zeigst deinen Ausweis und der Wärter lässt dich nach einem prüfenden Blick passieren.")

