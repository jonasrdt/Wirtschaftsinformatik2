PI = 3.1415 # Globale Variable

# Funktion zum Berechnen des Kreisumfangs
def kreisumfang(radius):
    kreisumfang_berechnet = 2 * PI * radius
    return kreisumfang_berechnet

def zylinder(radius, hohe):
    zylinder_berechnet = hohe * kreisumfang(radius)
    return zylinder_berechnet

print(zylinder(350, 100))