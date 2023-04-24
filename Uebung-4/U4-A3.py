


# range(start, stop, step)

zaehlvariable = 9

# This is code called `pascal()` that prints out a Pascal's triangle with a height of
# `zaehlvariable`. The first `for` loop iterates through each row of the triangle, the second `for`
# loop prints out the necessary spaces before the numbers in each row, the third `for` loop prints out
# the ascending numbers in each row, and the fourth `for` loop prints out the descending numbers in
# each row. The `print()` function is used to move to the next line after each row is printed.
for auesserer_zaehler in range(1,zaehlvariable+1):
    for z in range(zaehlvariable-auesserer_zaehler):
        print(" ", end=" ")
    for innerer_zaehler in range(1,auesserer_zaehler+1):
        print(innerer_zaehler, end=" ")
    for i in range(auesserer_zaehler-1, 0, -1):
        print(i, end=" ")
    print()