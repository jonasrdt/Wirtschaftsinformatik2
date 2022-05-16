# Entwicklen Sie ein Programm, welches die Anzahl der Wörter sowie die durchschnittliche
# Wortlänge eines durch den Nutzer eingegebenen Satzes berechnet, ausgibt und auf zwei
# Nachkommastellen rundet.

def textReplace(text, rep1, rep2):
    text = text.replace(rep1, "").replace(rep2, "")
    return text

def textSplit(text):
    woerter = text.split(" ")
    return woerter

def wordCount(woerter):
    print("In dem Text kommen folgende Wörter vor: ", woerter)
    print("In dem Text kommen insgesamt:", len(woerter), "Wörter vor.")
    return len(woerter)

def wordLength(text, anzahl_woerter):
    text = text.replace(" ", "")
    durchschnittliche_wortlaenge = round(len(text) / anzahl_woerter, 2)
    return durchschnittliche_wortlaenge

###########################
###### Hauptprogramm ###### 
###########################

text = input("Bitte geben Sie einen Satz ein: ") # Eingabe durch den User
text = textReplace(text, ".", ",") # Ersetzen von Punkt und Komma in dem Satz des Users
woerter = textSplit(text) # Splitten des Satzes des Users an den Leerzeichen
anzahl_woerter = wordCount(woerter) # Zählen der Liste mit den Wörtern des Users
print("Die durchschnittliche Wortlänge beträgt:", wordLength(text, anzahl_woerter), "Zeichen.")