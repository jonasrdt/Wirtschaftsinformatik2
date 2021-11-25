b = 5 # integer
c = 5.5 # float
d = True # boolean
e = [1, 2, 3] # liste
f = {'a': 2, 'b': 3} # Dictionary
g = "Hello there" # String

# Ändern des Datentypen von 'string' in 'int', damit wir damit rechnen können
alter = int(input("Bitte geben Sie Ihr Alter ein: "))

# Willkürliche Berechnung, die nur möglich ist wenn 'alter' vom Typ 'int' und nicht mehr vom Typ 'string' ist
irgendeine_berechnung = alter + 15
print(irgendeine_berechnung)
