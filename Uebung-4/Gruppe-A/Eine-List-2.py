mitarbeiter_kartei = ["Jonas", "Reinhardt", 30, 88.5, True]    # Datentyp: Liste (list)


# The code is iterating over each element in the list `mitarbeiter_kartei` and printing each element
# on a new line.
for element in mitarbeiter_kartei:
    print(element)
    
print("----------------------------------------")
# This code is iterating over a range of numbers from 0 to 1 (2 is not included) using a for loop. For
# each number in the range, it is using the number as an index to access the corresponding element in
# the list `mitarbeiter_kartei` and printing it. In this case, it will print the first two elements of
# the list, which are "Jonas" and "Reinhardt".
for i in range(0,2):
    print(mitarbeiter_kartei[i])