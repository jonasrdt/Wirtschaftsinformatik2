
# It splits the sentence into a list of words.
satz = "Success doesn't make you a better person, it just makes you a more successful person."
satz_splitted = satz.split(" ")
print(satz_splitted)
print("In dem Satz befinden sich", len(satz_splitted) ,"Wörter.")

# Replacing all the special characters in the list with an empty string.
sonderzeichen = [" ", ".", ",", ";", "/", "?", "!", ":", "€", "$", "§", "=", "#", "-", "_", "'"]
for element in sonderzeichen:
    satz = satz.replace(element, "")

# Calculating the average word length.
durchschnittslaenge_wort = round(len(satz) / len(satz_splitted),2)
print("Die durchschnittliche Wortlänge beträgt:", durchschnittslaenge_wort, "Zeichen.")