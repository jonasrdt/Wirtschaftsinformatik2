# Queue = lineare Datenstruktur --> Daten nach FIFO-Prinzip verwaltet 
# Ankommen --> Enqueue = Element am Ende der Queue einfügen
# Verlassen --> dequeue = erstes Element aus Queue löschen. Implementiert durch .pop(Listenposition)

# Person kommt an:
# --> Definition: Person am Ende der Queue durch enqueue über append Funktion hinzufügen
def enqueue(x): 
    Warteschlange.append(x) 

# Person verlässt:
# --> erste Person/ Element von Queue an Position 0 der Liste löschen.
# Erstes Elemet löschen durch Implementieren von dequeue über .pop Funktion
def dequeue(x): 
    Warteschlange.pop(0) 

# Liste erzeugen
Warteschlange = []

# Personen kommen an --> Personen als Elemente der Liste hinzufügen nach FiFo.
enqueue("Alina")
print("Alina kommt an")
enqueue("Bernd")
print("Bernd kommt an")
enqueue("Christoph")
print("Christoph kommt an")
print("Die Warteschlange ist", Warteschlange)

# Personen verlassen --> Personen als Elemente der Liste löschen nach FiFo.
dequeue("Alina")
print("Alina verlässt die Warteschlange")
dequeue("Bernd")
print("Bernd verlässt die Warteschlange")
dequeue("Christoph")
print("Christoph verlässt die Warteschlange")