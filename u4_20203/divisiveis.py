# Quantidade de Inteiros Divisíveis por K


k = int(input())
quantidade_de_numeros = int(input())

numeros = [] 

for _ in range(quantidade_de_numeros): 
    n = int(input())
    numeros.append(n)

divisiveis = [] 
cont = 0 

for n in range(len(numeros)):
    if numeros[n] % k == 0: 
        cont += 1


print("{} ({:.1f}%)".format(cont, (cont / quantidade_de_numeros)*100))
