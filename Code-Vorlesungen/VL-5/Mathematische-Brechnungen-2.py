PI = 3.1415 # Globale Variable, leben im ganzen Programm und können von überall benutzt werden

# Die Funktion 'kreisumfang' berechnet den Kreisumfang auf Basis eines eingegebenen Radius
def kreisumfang(radius):
    kreisumfangBerechnung = 2 * PI * radius # lokale Variable, die nur in der Funktion lebt und nur von dort aus benutzt werden kann
    return kreisumfangBerechnung # lokale Variable, die nur in der Funktion lebt und nur von dort aus benutzt werden kann

def zylinder(radius, hoehe):
    return hoehe * kreisumfang(radius)

print(zylinder(50,20))
