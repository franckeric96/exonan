a = input("entrez un nombre :")
while not a.isdigit():
    a = input("entrez un nombre :")
while int(a) < 1 or int(a) > 3 :
    a =input("entrez un nombre compris entre 1 et 3 :")
print("tu l'as enfin trouver")
