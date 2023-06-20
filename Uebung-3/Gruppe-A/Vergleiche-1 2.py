familienstand = input("Bitte geben Sie Ihren Familienstand (ledig/verheiratet) an: ")

if familienstand.lower() == "verheiratet":
    print("Sie sind verheiratet")
elif familienstand.lower() == "ledig":
    print("Sie sind ledig.")
else:
    print("Sie sind weder ledig, noch verheiratet.")