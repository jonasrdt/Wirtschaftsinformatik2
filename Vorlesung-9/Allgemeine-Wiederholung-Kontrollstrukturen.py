
# Einfach Zuweisung von Integer Variablen
a = 3
b = 5
c = 10

# Verknüpfen der Kontrollstruktur mit elif, damit
# eine zusammenhängende Betrachtung stattfindet
# und die Statements nicht isoliert voneinander
# ausgeführt werden.
if a > b:
    print(a, "ist größer als", b)
elif a < b:
    print(a, "ist kleiner als", b)
elif a < c:
    print(a, "ist kleiner als", c)
elif a > c:
    print(a, "ist größer als", c)
else:
    print("Keiner der Zustände trifft zu.")