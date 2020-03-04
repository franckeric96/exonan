#fonction
def amende(p,c,v,a):
    pperdu = p + 3*c + 5*v + 10*a
    return (pperdu*200)/100

#ce programme permet de donnée le nombre de victime
poule = int(input("entrez le nombre de poule tuer:"))
chien = int(input("entrez le nombre de chien tuer:"))
vache = int(input("entrez le nombre de vache tuer:"))
ami = int(input("entrez le nombre d'ami tuer:"))

payer = amende(poule,chien,vache,ami)
print("rien à payer") if payer == 0 else print("le montant à payer est",payer,"euros")
    