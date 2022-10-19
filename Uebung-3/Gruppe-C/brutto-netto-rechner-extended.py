

familienstand = input("Bitte geben Sie Ihren Familienstand an: ")
print("Der von Ihnen eingegeben Familienstand ist:", familienstand)

if familienstand.lower() == "ledig":
    print("Heiratet lohnt sich allein schon steuerlich.")
else:
    print("Immer schön ans Ehegatten-Splitting denken.")
    