a = int(input("entrez un entier:"))
k = 1
f = 1
while a < 0 :
    a = int(input("entrez un entier positif:"))

while k <= a:
    f = f*k
    k = k + 1
print("le factoriel de",a,"est:",f)