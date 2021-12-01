

#       0 1 2 3 4 5 6 7 (8) 9 10 11 12 13 14
name = "Robinson? !Crusoe,"
print(name)
ueberspringe = [",", "!", "?", ";"] 
for char in name:
    if char in ueberspringe:
        name = name.replace(char, "")
print(name)
