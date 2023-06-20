

tante_emma = {
    "Brot": 5,
    "Käse": 10,
    "Wurst": 2,
    "Bier": 10
}

eingabe = input("Bitte geben Sie ein, was Sie aus dem Tante Emma Laden haben wollen: ")
if eingabe in tante_emma:
    print("Das haben wir :-).")
else:
    print("Das haben wir nicht.")
    