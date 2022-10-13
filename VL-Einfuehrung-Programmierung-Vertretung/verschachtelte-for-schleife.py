
anzahl_zeilen = int(input("Bitte geben Sie die Anzahl der Zeilen an: "))
anzahl_spalten = int(input("Bitte geben Sie die Anzahl der Spalten an: "))
user_zeichen = input("Bitte geben Sie ein Zeichen ein: ")

for zeilen in range (1, anzahl_zeilen + 1):
    for spalten in range (1, anzahl_spalten + 1):
        print(user_zeichen, end= " ")
    print()