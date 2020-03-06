a = input("entrez un nombre :")
while not a.isdigit():
    a = input("entrez un nombre :")
while int(a) < 10 or int(a) > 20 :
    if int(a)>20:
        print("plus petit!")
    elif int(a)<10:
        print("plus grand")
    a =input("entrez un nombre compris entre 10 et 20 :")
print("tu l'as enfin trouvez")

