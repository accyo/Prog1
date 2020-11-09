# MEDIA DOS PARES

n = int(input())
numeros = [] 

soma = 0
pares = 0 

abaixo_media = [] 

for _ in range(n): 
    
    numero = int(input())
    numeros.append(numero)

for i in range(len(numeros)):

    if numeros[i] % 2 == 0:
        soma += numeros[i]
        pares += 1

media = soma / pares

for e in range(len(numeros)):
    
    if numeros[e] < media: 
        abaixo_media.append(numeros[e])


print("soma: {}".format(soma))
print("média: {:.1f}".format(media))
print("{} número(s) abaixo da média".format(len(abaixo_media)))
