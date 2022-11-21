

telefonbuch = [["Miray", "990129030"],
               ["Nicolas", "89398123"],
               ["Bennett", "908423783"],
               ["Jaqueline", "089922343"],
               ["Jonas", "2190818924"]]

name = input("Bitte geben Sie den Namen ein, dessen Telefonnummer Sie erfahren möchten: ")

for eintrag in telefonbuch:
    if eintrag[0] == name:
        print("Die Telefonnummer von", name,"lautet", eintrag[1])
        break # Schleife bewusst abbrechen, wenn Name gefunden wurde