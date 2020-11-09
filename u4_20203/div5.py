# SOMA DIVISORES DE 5 

n = int(input())

numeros = []
soma = 0 

for _ in range(n):     
    numeros.append(int(input()))


for i in range(len(numeros)): 

    if numeros[i] % 5 == 0: 
        soma += numeros[i]


print(soma)
