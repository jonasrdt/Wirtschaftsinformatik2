# Merke: Eine Liste muss im Zweifel komplett durchsucht werden => Komplexität O(n)
# Beim Dictionary erfolgt ein Direktzugriff => Komplexität O(1)

telefon_liste = [['Jonas', '9310923'],
                 ['Peter', '3908239'],
                 ['Sina', '3192033']]

name_liste = input("Bitte geben Sie den Namen ein, zu dem Sie die Telefonnummer haben wollen: ")
for entry in telefon_liste:
    if entry[0] == name_liste:
        print(entry[1])

telefon_dict = {
    'Jonas': '9310923',
    'Peter': '3908239',
    'Sina': '3192033'
}

name_dict = input("Bitte geben Sie den Namen ein, zu dem Sie die Telefonnummer haben wollen: ")
if name_dict in telefon_dict:
    print(telefon_dict[name_dict])
