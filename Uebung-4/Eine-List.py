

name = "Jonas"          # Datentyp: String (str)
alter = 30              # Datentyp: Integer (int)
gewicht = 88.5          # Datentyp: Float (float)
brillentraeger = True   # Datentyp: Boolean (bool)

# The code is creating a list called `mitarbeiter_kartei` with different data types such as string,
# integer, float, and boolean. It is printing the element at index 1 of the list, which is
# "Reinhardt". After that, it is printing the length of the list using the `len()` method.

# Index                 0          1        2    3     4
mitarbeiter_kartei = ["Jonas", "Reinhardt", 30, 88.5, True]    # Datentyp: Liste (list)

# Zugreifen auf das Element am Index 1 => Reinhardt
print(mitarbeiter_kartei[1])

# Ausgeben der Länge der Liste mithilfe der len()-Methode
print(len(mitarbeiter_kartei))


print(mitarbeiter_kartei)
mitarbeiter_kartei.append("1.15")
print(mitarbeiter_kartei)
mitarbeiter_kartei.pop(1)
print(mitarbeiter_kartei)