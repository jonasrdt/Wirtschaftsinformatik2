
# Initialisieren der Variablen
word_count = 0
char_count = 0

# Eingabe des Nutzers empfangen
nutzereingabe = input("Bitte geben Sie einen Satz ein: ")

# Aufteilen der Nutzereingabe mithilfe von split()
split_string = nutzereingabe.split()

# Zählen der Wörter mithilfe von len()
word_count = len(split_string)

# Zählen der Buchstaben, indem die Liste mit den Wörtern durchgegangen und die länge eines jeden Wortes gezählt wird
for word in split_string:
    char_count += len(word)

# Berechnen der durchschnittlichen Wortlänge, in dem die Anzahl der Buchstaben durch die Anzahl der Wörter geteilt wird
average_words = round(char_count / word_count,0)

# Ausgabe der ermittelten Inhalte
print("Anzahl der Wörter: {}".format(word_count))
print("Gesamtanzahl der Buchstaben: {}".format(char_count))
print("Durchschnittliche Anzahl der Buchstaben: {}".format(int(average_words)))