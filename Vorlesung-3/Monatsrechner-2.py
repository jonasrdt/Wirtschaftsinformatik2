# Der Nutzer soll eine Zahl eingeben können
# und das Programm gibt aus, wie viele
# Tage der jeweilige Monat hat

# Folgender Code soll solange durchlaufen, bis der Nutzer ein 0 gibt
# Festlegen eines Wertes für monat, der nicht 0 ist, damit die Schleife startet
monat = 1

while monat != 0:
        # Nutzereingabe abfragen
        monat = int(input("Bitte geben Sie einen Monat ein (1-12) oder eine 0 wenn Sie das Programm beenden wollen: "))
        if (monat == 1 or monat == 3 or monat == 5 or monat == 7 or monat == 8 or monat == 10 or monat == 12):
            print("Der Monat", monat, "hat 31 Tage.")
        elif (monat == 2):
            print("Der Monat", monat,"hat 28 Tage.")
        elif (monat == 0):
            print("Okay, das Programm wird beendet.")
        elif (monat == 4 or monat == 6 or monat == 9 or monat == 11):
            print("Der Monat", monat, "hat 30 Tage.")
        else:
            print("Bitte geben Sie nur Zahlen zwischen 1 und 12 ein.")


# # # # # # #  # # # #
# # Alternativlösung:
# # # # # # #  # # # #  
# monat = 1
# while monat != 0:
#     # Nutzereingabe abfragen
#     monat = int(input("Bitte geben Sie einen Monat ein (1-12) oder eine 0 wenn Sie das Programm beenden wollen: "))
#     if (1 <= monat <= 12):
#         if (monat == 1 or monat == 3 or monat == 5 or monat == 7 or monat == 8 or monat == 10 or monat == 12):
#             print("Der Monat", monat, "hat 31 Tage.")
#         elif (monat == 2):
#             print("Der Monat", monat,"hat 28 Tage.")
#         elif (monat == 0):
#             print("Okay, das Programm wird beendet.")
#         else:
#             print("Der Monat", monat, "hat 30 Tage.")
#     else:
#         print("Bitte nur Zahlen zwischen 1 und 12 eingeben.")