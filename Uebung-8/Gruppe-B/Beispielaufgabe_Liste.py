# Ergänzen Sie die folgende Funktion so, dass das Programm nicht abstürzt
# wenn sich keine Personen in der Warteschlange befinden. Stattdessen soll
# ausgegeben werden "Es befinden sich keine Personen in der Warteschlange.".

### LÖSUNGSMÖGLICHKEIT 1

def verlassen():
    # Ergänzen Sie hier Ihre Lösung
    try:    
        print("Person:", warteschlange[0], "wurde aufgerufen und wird jetzt entfernt.")
        warteschlange.pop(0)
    except:
        print("Es befinden sich keine Personen in der Warteschlange.")
        
### LÖSUNGSMÖGLICHKEIT 2
 
def verlassen():
    # Ergänzen Sie hier Ihre Lösung
    if len(warteschlange) > 0:   
        print("Person:", warteschlange[0], "wurde aufgerufen und wird jetzt entfernt.")
        warteschlange.pop(0)
    else:
        print("Es befinden sich keine Personen in der Warteschlange.")
