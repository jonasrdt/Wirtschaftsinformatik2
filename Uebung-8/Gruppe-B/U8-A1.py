# Erstellen Sie ein Python-Programm mit den folgenden Anforderungen.
# a) Der Anwender soll dazu aufgefordert werden, einen beliebigen Satz einzugeben, z. B.
# „Der Hund läuft in die Küche“
# b) Erstellen Sie eine Funktion, welche analysiert, wie viele Wörter in dem Satz
# vorkommen.
# c) Erstellen Sie eine Funktion, welche analysiert, wie die durchschnittliche Wortlänge im
# Satz ist.

# This code is prompting the user to input a sentence and storing it in the variable `satz`. Then, the
# sentence is split into a list of words using the `split()` method and stored in the variable
# `satz_splitted`. The number of words in the sentence is then calculated using the `len()` function
# and stored in the variable `anzahl_woerter`.
satz = input("Bitte geben Sie einen beliebigen Satz ein: ")
satz_splitted = satz.split(" ")
anzahl_woerter = len(satz_splitted)
# This code is creating a list of special characters called `sonderzeichen` and then iterating through
# each element in the list using a `for` loop. For each element, it is removing that character from
# the `satz` string using the `replace()` method. This is done to remove any special characters from
# the sentence before analyzing the number of words and average word length.
sonderzeichen = [" ", ".", ",", "!", "?", "§", "$", "%", "&", "/", "(", ")", "=", "-"]
for element in sonderzeichen:
    satz = satz.replace(element, "")
print(satz)
# This code is calculating the length of the sentence without any special characters and storing it in
# the variable `laenge_satz`. Then, it is calculating the average word length by dividing
# `laenge_satz` by the number of words in the sentence (`anzahl_woerter`) and rounding the result to 2
# decimal places using the `round()` function. Finally, it is printing out the number of words and the
# length of the sentence, as well as the average word length.
laenge_satz = len(satz)
durchschnittliche_wortlaenge = round(laenge_satz / anzahl_woerter,2)
print("Der Satz enthält", anzahl_woerter, "Wörter. Und", laenge_satz, "Anzahl Zeichen.")
print("Das durchschnittliche Wort ist:", durchschnittliche_wortlaenge, "Zeichen lang.")


####################################################################################
# Mögliche Aufgabenstellung:
# Ergänzen Sie folgende Funktion so, dass alle Sonderzeichen aus dem Paramter 'satz' entfernt werden

# def removesonderzeichen(satz):
#     sonderzeichen = [" ", ".", ",", "!", "?", "§", "$", "%", "&", "/", "(", ")", "=", "-"]
#     # Ergänzen Sie hier Ihre Lösung
#     for element in sonderzeichen:
#         satz = satz.replace(element, "")
#     return satz