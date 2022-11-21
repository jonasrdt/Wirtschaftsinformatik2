count = 1
dict = {}
def c():
    for counter in range(3):
        dict.update({"Counter": counter})
    return counter
c()
print(dict["Counter"])