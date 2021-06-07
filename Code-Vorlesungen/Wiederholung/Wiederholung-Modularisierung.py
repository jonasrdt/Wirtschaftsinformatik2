def nutzereingabesplit(nutzereingabe):
    # Aufteilen der Nutzereingabe mithilfe von split()
    split_string = nutzereingabe.split(" ")
    return split_string

def wordcount(split_string):
    # Zählen der Wörter mithilfe von len()
    word_count = len(split_string)
    return word_count

def charcount(split_string):
    # Zählen der Buchstaben, indem die Liste mit den Wörtern durchgegangen und die länge eines jeden Wortes gezählt wird
    char_count = 0
    for word in split_string:
        char_count += len(word)
    return char_count

def averagewords(char_count, word_count):
    # Berechnen der durchschnittlichen Wortlänge, in dem die Anzahl der Buchstaben durch die Anzahl der Wörter geteilt wird
    average_words = round(char_count / word_count,0)

# Eingabe des Nutzers empfangen
satz = input("Bitte geben Sie einen Satz ein: ")
print("Das ist der gesplittet String", nutzereingabesplit(satz))
split_string = nutzereingabesplit(satz)
print("Der eingegeben Satz beinhaltet", wordcount(split_string), "Wörter.")


