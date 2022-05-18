

mitglieder = [["Jonas", 29, 1.91], # 0
              ["Alex", 32, 1.84], # 1
              ["Emil", 23, 1.86]] # 2

staedte = [["Paris", "FR", 2.161], # 0
           ["Rom", "IT", 2.873], # 1
           ["Berlin", "DE", 3.645]] # 2 

for stadt in staedte:
    print("Es gibt die Stadt:", stadt[0])
    print("Sie hat", stadt[2] , "Einwohner.")
    print("Sie liegt in dem Land:", stadt[1])
    print("-----------------------------------")
