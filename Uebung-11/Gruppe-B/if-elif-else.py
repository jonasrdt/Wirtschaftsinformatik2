gueltige_fahrkarte = False
bargeld = True

if gueltige_fahrkarte or bargeld:
    print("Sie dürfen mitfahren.")
else:
    print("So können Sie leider nicht mitfahren.")


# Abfragen mehrerer Zustände mit if-elif-else,
# um die Verknüpfung zu einer Gesamtabfrage zu erstellen.
semestererfahrung = 1
if 0 <= semestererfahrung < 2:
    print("Sie erhalten 85€ pro SWS.")
elif 2 <= semestererfahrung <= 4:
    print("Sie erhalten 95€ pro SWS.")
elif semestererfahrung <= 5:
    print("Sie erhalten 105€ pro SWS.")
else:
    print("Ihre Erfahrung kann keiner Stufe zugeordnet werden.")

# if-elif-else mit Nutzereingabe und .lower()
# .lower() sorgt dafür, dass alle Zeichen in der
# Variable kleingeschrieben werden.
entscheidung = input("Wollen Sie weiterspielen (ja/nein): ")
if entscheidung.lower() == "ja":
    print("Okay, es wird weitergespielt.")
elif entscheidung.lower() == "nein":
    print("Okay, wir beenden das Spiel.")
else:
    print("Ihre Entscheidung konnte nicht zugeordnet werden.")
    
    
# Beispielaufgabe: Schreiben Sie eine if-elif-else Abfrage welche prüft,
# ob das Alter des Nutzers größer als 18 ist. Wenn nicht, soll 'Heute nicht'
# ausgegeben werden, andernfalls 'Du darfst rein'

alter = 15
# Fügen Sie nachfolgend Ihre Lösung ein
if alter > 18:
    print("Du darfst rein.")
elif alter < 18:
    print("Heute nicht.")
else:
    print("Das Alter kann nicht zugeordnet werden.")