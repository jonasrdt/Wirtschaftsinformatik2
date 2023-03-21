weiterer_artikel = False
# Bool'sche Variable, um zu vermerken, ob ein Artikel vorhanden ist
vorhanden = True

while not weiterer_artikel:
    einkauf = [["Bier", 2.5], ["Sekt", 6], ["Wein", 8]]

    eingabe = "Bier"
    for i, inner_list in einkauf:
        if eingabe == i:
            print(eingabe, "ist vorhanden.")

        


#     eingabe = input( "Was suchen Sie ?: ")
#     # Prüfen, ob der Artikel in der Liste vorhanden ist
#     for artikel in einkauf:
#         if artikel[0] != eingabe:
#             vorhanden = False
#     # Man könnte auch schreiben if vorhanden != False
#     if not vorhanden:
#         print ("Der Artikel ist nicht vorhanden")
#         entscheidung = input ("Wollen Sie den Artikel hinzufügen ?: ")
#         if entscheidung. upper() == "JA":
#             preis = float (input("Bitte geben Sie den dazugehörigen Preis ein: "))
#             einkauf.append ([eingabe, preis])
#             print(einkauf)
    
#     if vorhanden:
#         for elemente in einkauf:
#             if eingabe == elemente[0]:
#                 print ("Der Artikel kostet", elemente[1],"€")
            
#     neue_suche = input ("Möchten Sie noch einen Artikel suchen ?: ")
#     if neue_suche.upper() == "NEIN" :
#         weiterer_artikel = True
# print("Programm beendet")