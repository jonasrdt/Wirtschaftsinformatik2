
# Technische Fehlerabfrage mit try,except.
# Gibt der Nutzer etwas ein, dessen Datentyp nicht geändert werden kann
# bricht das Programm nicht mit einem Fehler, sondern mit dem Inhalt
# in 'except' ab.
try:
    # Anlegen der Variable 'alter' und ändern des
    # Datentyps von String (str) auf Integer (int)
    alter = int(input("Bitte geben Sie Ihr Alter ein: "))
    
    # Inhaltliche Prüfung ('Fehlerabfrage'), falls
    # der Nutzer eine inhaltlich nicht korrekte Eingabe
    # tätigt.
    if 0 < alter < 125:
        print("Sie haben ein korrektes Alter eingegeben.")
    else:
        print("Bitte geben Sie ein valides Alter zwischen 0 und 125 Jahren an.")
except:
    print("Bitte geben Sie nur Zahlen ein.")
    

