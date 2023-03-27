# Schreiben Sie ein kleines Python-Programm, das auf Basis des Geburtsjahres
# berechnet, wie alt die Person heute ist.
# Beispiel:
# Wann bist du geboren: 1992
# Wenn du 1992 geboren bist, bist du heute 31 Jahre alt.

# It imports the datetime module.
import datetime

# Asking the user for their birth year and then calculating their age.
aktuelles_jahr = datetime.date.today().year
# Asking the user for their birth year and then converting it to an integer.
geburtsjahr = int(input("In welchem Jahr bist du geboren: "))
# Subtracting the current year from the birth year.
alter = aktuelles_jahr - geburtsjahr
# Verkettete Mehrfachausgabe mit print(). Wichtig: Trennen der Inhalte durch ein Komma!
print("Wenn du", geburtsjahr, "geboren bist, bist du", alter, "Jahre alt.")