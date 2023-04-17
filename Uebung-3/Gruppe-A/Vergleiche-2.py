

weitermachen = "ja"

while weitermachen.lower() == "ja":
    print("Es wird immer weitergemacht.")
    weitermachen = input("Sollen wir weitermachen: ")
print("Die Schleife wurde abgebrochen, weil für die Variable weitermachen", weitermachen, "eingegeben wurde.")