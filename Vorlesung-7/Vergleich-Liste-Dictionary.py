
# Adressbuch als Dictionary mit einer Komplexität O(1)
adressbuch = {
    "Lara" : "05761496961",
    "Jan" : "0611135160"
}
print("Die Telefonnummer von Lara lautet:", adressbuch["Lara"])

# Adressbuch als verschachtelte Liste mit einer Komplexität O(n)
adressbuch = [
    ["Lara","05761496961"],
    ["Jan","0611135160"],
]
for element in adressbuch:
    if element[0] == "Lara":
        print("Die Telefonnummer von Lara lautet:", element[1])


