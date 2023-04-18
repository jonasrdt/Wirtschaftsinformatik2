
weitermachen = "ja"

while weitermachen.lower() == "ja":
    print("Die Schleife wird immer weiter ausgeführt.")
    weitermachen = input("Soll die Schleife weiter ausgeführt werden (ja/nein): ")
print("Die Schleife wurde abgebrochen, weil für weitermachen:", weitermachen, "eingegeben wurde.")