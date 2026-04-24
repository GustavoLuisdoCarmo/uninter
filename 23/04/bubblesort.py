numero = [6,7,5,1,2]
n = len(numero)
for i in range(n):
    for j in range(0,n-i-1):
        if numero[j] > numero [j+1]:
            numero[j],numero[j+1] = numero[j+1], numero[j]

print(numero)