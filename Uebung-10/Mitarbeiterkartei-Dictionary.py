
mitarbeiterkartei = {}
error_counter = 0

richtige_eingabe = False
while not richtige_eingabe:
    namen = input("Bitte geben Sie Ihren Vor- und Nachname ein: ")
    wrong_chars = ["!", ".", ",", "0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]
    for char in wrong_chars:
        if char in namen:
            print("Bitte geben Sie nur Buchstaben ein.")
            error_counter += 1
            print(wrong_chars.index(char))
        elif wrong_chars.index(char) == (len(wrong_chars) -1) and error_counter == 0:
            print("Sie haben einen gültigen Namen eingegeben.")
            richtige_eingabe = True
            break;


# Jonas Reinhardt
namen = namen.split(" ")
#   0        1
# ['Jonas', 'Reinhardt']
mitarbeiterkartei.update({'Vorname': namen[0]})
mitarbeiterkartei.update({'Nachname': namen[1]})
print(mitarbeiterkartei)
# {
# 'Vorname' : 'Jonas',
# 'Nachname' : 'Reinhardt'  
# }
geburtsort = input("Bitte geben Sie Ihren Geburtsort an: ")
mitarbeiterkartei.update({'Geburtsort': geburtsort})
# {
# 'Vorname' : 'Jonas',
# 'Nachname' : 'Reinhardt',
# 'Geburtsort' : 'Kiel'
# }
print(mitarbeiterkartei)