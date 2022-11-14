
staedte = ["Paris", "Athen", "Kiel", "Berlin", "Cancun"]

for stadt in staedte:
    print(stadt)

neue_stadt = input("Bitte geben Sie die Stadt ein, die Sie hinzufügen wollen: ")
staedte.append(neue_stadt)

for stadt in staedte:
    print(stadt)