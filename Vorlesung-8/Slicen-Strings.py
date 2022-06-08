    #   0 1 2 3 4 5 6 7 8 9 10 11 12 13 14
    #   M a n c h e   L e u c  h  t  e  n 
satz = "Manche Leuchten, wenn man sie liest."
print(satz[:15])
# Was kommt raus?

satz = "Manche Leuchten, wenn man sie liest."
satz_splitted = satz.split(" ")

replace = [".", ",", "-", "?", " "]
for element in replace:
    satz = satz.replace(element, "")

print("Der Satz hat", len(satz) ,"Zeichen.")
print("Der Satz enthält:", len(satz_splitted), "Wörter.")
# Was muss ergänzt werden?

