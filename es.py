lista = [1,2,3,4,5,9]
#stampa
for x in lista:
    print (x)
print('-------------------------------------------')

#somma
a = 0
for x in lista:
    a += x
print(a)
print('---------------------------------------')

#media
a=0
b=0
for x in lista:
    a+=x
    b+=1
print(a/b)
print('---------------------------------------')

#minimo
a=lista[1]
for x in lista:
    if a>=x:
        a=x
print (a)
print('---------------------------------------')

#massimo
a=lista[1]
for x in lista:
    if a<=x:
        a=x
print (a)
print('---------------------------------------')

vettore1 = [1,2,3]
vettore2 = [4,5,6]
#sommma.vet1
for x in vettore1:
    if x%1!=0:
        print("il vettore 1 contiene numeri non interi")
        raise Exception
for x in vettore2:
    if x%1!=0:
        print("il vettore 1 contiene numeri non interi")
        raise Exception

a=0
for x in vettore1:
    a+=1
b=a
for x in vettore2:
    a-=1
if a == 0:
    cont = 0
    while cont<b:
        somma=vettore1[cont]+vettore2[cont]
        print(somma)
        cont+=1
else:
    print('i due vettori hanno dimensioni differenti')
    raise Exception
print('---------------------------------------')

vettore1 = [1,2,3]
vettore2 = [4,5,6]
#sommma.vet2
for x in vettore1:
    if x%1!=0:
        print("il vettore 1 contiene numeri non interi")
        raise Exception
for x in vettore2:
    if x%1!=0:
        print("il vettore 1 contiene numeri non interi")
        raise Exception

a=0
for x in vettore1:
    a+=1
b=a
for x in vettore2:
    a-=1
if a == 0:
    cont = 0
    while cont<b:
        vettore1[cont]+=vettore2[cont]       
        cont+=1
    print(vettore1)
else:
    print('i due vettori hanno dimensioni differenti')
    raise Exception

print('---------------------------------------')
vettore1 = [1,2,3]
vettore2 = [4,5,6]
#prodetto.vet1
for x in vettore1:
    if x%1!=0:
        print("il vettore 1 contiene numeri non interi")
        raise Exception
for x in vettore2:
    if x%1!=0:
        print("il vettore 1 contiene numeri non interi")
        raise Exception

a=0
for x in vettore1:
    a+=1
b=a
for x in vettore2:
    a-=1
if a == 0:
    cont = 0
    while cont<b:
        prodotto=vettore1[cont]*vettore2[cont]
        print(prodotto)
        cont+=1
else:
    print('i due vettori hanno dimensioni differenti')
    raise Exception
print('---------------------------------------')
vettore1 = [1,2,3]
vettore2 = [4,5,6]
#prodetto.vet2
for x in vettore1:
    if x%1!=0:
        print("il vettore 1 contiene numeri non interi")
        raise Exception
for x in vettore2:
    if x%1!=0:
        print("il vettore 1 contiene numeri non interi")
        raise Exception

a=0
for x in vettore1:
    a+=1
b=a
for x in vettore2:
    a-=1
if a == 0:
    cont = 0
    while cont<b:
        vettore1[cont]=vettore1[cont]*vettore2[cont]
        cont+=1
    print(vettore1)
else:
    print('i due vettori hanno dimensioni differenti')
    raise Exception
    

