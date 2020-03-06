E = 1 
sommedue = 0
while E != 0:
    E = int(input("entrer le montant:"))
    sommedue = sommedue + E
print("vous devez:",sommedue,"euros")
M = int(input("Montant versé:"))
reste = M - sommedue
nb = 0
while reste >= 10:
    nb = nb + 1
    reste = reste - 10
nbE = 0
if reste >= 5:
    nbE = 5
    reste = reste - 5

print("rendu de la monnaie:")
print("billet de 10 E:", nb)
print("billet de 5 E:", nbE)
print("pièce de 1 E:", reste)

