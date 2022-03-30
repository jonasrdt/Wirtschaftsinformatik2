# In Abhängigkeit von der Menge soll ein Rabatt berechnet werden
# 10 Stück = 5% Rabatt
# 20 Stück = 10% Rabatt
# 30 Stück = 15% Rabatt

menge = int(input("Bitte geben Sie die zu kaufende Menge ein, um den Rabatt zu berechnen: "))

if (10 <= menge < 20):
    print("Sie bekommen 5% Rabatt.")
elif (20 <= menge < 30):
    print("Sie bekommen 10% Rabatt.")
elif (menge >= 30):
    print("Sie bekommen 15% Rabatt.")
else:
    print("Sie bekommen keinen Rabatt.")