PI = 3.1415 # Globale Variable

def kreisumfang(radius):
    kreisumfang = 2 * PI * radius
    return kreisumfang

def zylinder(radius, hoehe):
    return hoehe * kreisumfang(radius)

print(zylinder(50, 20))