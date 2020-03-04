prix = float(input("entrez le prix unitaire d'une heure :"))
nbheures = int(input("combien d'heure suplémentaire avez vous réaliser? "))
montant = 0

if nbheures <= 39 :
    montant = 0
elif nbheures < 45 :
    montant = (nbheures -39)*(prix*1.5)
    
elif nbheures < 50 :
    montant = (5*prix*1.5)+(nbheures -44)*(prix*1.75)
else:
    montant =(5* prix *1.5)+(5* prix *1.75)+( nbheures -49)*( prix *2)
print("le montant des heures suplémentaire est:",montant)