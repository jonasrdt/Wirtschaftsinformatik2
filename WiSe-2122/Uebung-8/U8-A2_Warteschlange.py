# Im Einwohnermeldeamt soll ein neues System implementiert werden.
# Ankommende Besucher müssen sich mit ihrem Namen anmelden. Jeder weitere Besucher stellt sich danach
# „hinten“ an. Es entsteht ein Warteschlange (Liste). Die Besucher werden der Reihe nach aufgerufen
# und verlassen die Warteschlange (First-In-First-Out FIFO).

# Programmieren Sie eine Warteschlange mit folgenden Funktionen:
# • ankommen(name) (Eine Person stellt sich in die Warteschlange hinten an)
# • verlassen() (Die erste Person einer Warteschlange verlässt die Warteschlange)
# • ausgabe() (Die komplette Warteschlange wird als Liste ausgegeben).

# Initialisieren der Variable für die Liste
warteschlange = []
sessions = []
available_sessions = 5
used_sessions = 0

def ankommen_success(name):
    sessions.append(name)
    used_sessions += 1
    
def leave_success():
    sessions.pop(0)
    used_sessions -= 1

def ankommen(name):
    warteschlange.append(name)
    print(name, "kommt an.")
    
def alleVerlassen():
    for zaehler in range(len(warteschlange)):
        print(warteschlange[zaehler], "verlässt die Warteschlange.")
        
def einerVerlässt():
    print(warteschlange[0], "verlässt die Warteschlange.")
    warteschlange.pop(0)
    
def ausgabe():
    print("Die Warteschlange ist:", warteschlange)

benutzer = input("Wer will zugreifen: ")

if used_sessions < available_sessions:
    ankommen_success(benutzer)
    print("Herzlichen Glückwunsch, kaufen Sie Ihre Karte für Wacken 2023.")
    entscheidung = input("Wollen Sie die Website jetzt wieder verlassen (ja/nein): ")
    if entscheidung.lower() == "ja":
        leave_success()
else:
    print("Sie werden der Warteschlange hinzugefügt.")
    ankommen(benutzer)
    ausgabe()

