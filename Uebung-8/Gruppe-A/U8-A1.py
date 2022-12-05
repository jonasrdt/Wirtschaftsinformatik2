def anzahlWoerter(satz_gesplitted):
    """
    It takes a list of words and returns the number of words in the list
    
    :param satz_gesplitted: The sentence split into words
    :return: The number of words in the sentence.
    """
    return len(satz_gesplitted)

def anzahlZeichen(satz_bereinigt):
    """
    It takes a string as input and returns the number of characters in that string
    
    :param satz_bereinigt: The string that you want to count the characters in
    :return: The length of the string.
    """
    return len(satz_bereinigt)

def satzSplit(satz):
    """
    `satzSplit` takes a string and returns a list of the words in the string
    
    :param satz: The sentence to be split
    :return: A list of words
    """
    return satz.split(" ")

def satzBereinigen(satz):
    """
    It takes a string and removes all the characters in the list `ueberfluessige_zeichen` from it
    
    :param satz: The sentence to be cleaned
    :return: a string without any of the characters in the list ueberfluessige_zeichen.
    """
    ueberfluessige_zeichen = [".", ",", ";", ":", "!", "?", "-", "_", " "]
    for zeichen in ueberfluessige_zeichen:
        satz = satz.replace(zeichen, "")
    return satz

# Asking the user to input a sentence, then it splits the sentence into words, counts the number of
# words, cleans the sentence, counts the number of characters, and prints the number of characters and
# words.
nutzereingabe = input("Bitte geben Sie einen Satz ein: ")
satz_gesplitted = satzSplit(nutzereingabe)
anzahl_woerter = anzahlWoerter(satz_gesplitted)
satz_bereinigt = satzBereinigen(nutzereingabe)
anzahl_zeichen = anzahlZeichen(satz_bereinigt)
print("Der Satz hat", anzahl_zeichen, "Zeichen und", anzahl_woerter, "Wörter.")
print("Ein Wort ist im Durchschnitt also", round(anzahl_zeichen / anzahl_woerter, 2), "lang.")
