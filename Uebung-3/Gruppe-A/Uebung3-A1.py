# CMD + K + U = Einkommentieren
# CMD + K + C = Auskommentieren
# Unter Windows statt CMD einfach STRG einsetzen

x = 5
y = 10
z = 10

print(x < y) # True
print(y < z) # False
print(x==5) # True
print(not x == 5) # not negiert die Aussage. In diesem Fall wird "True" zu "False"
print(x != 5) # != Ungleichheit: Ist x ungleich 5? => False
print(not x != 5) # True, denn es ist "not False"
print(x == "5") # Vergleich von Datentyp Integer (int) und Datentyp String (str) => False
print(5 == x + 0.000000001) # False
print(x == 5 and y == 10) # True
print(x == 5 and y == 5) # False
print(x == 5 or y == 5) # True


