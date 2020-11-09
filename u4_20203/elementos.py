# SOMA ELEMENTOS A CADA K POSIÇÕES


posicoes = int(input())
n = int(input())

elementos = []

for _ in range(n): 
    e = int(input())
    elementos.append(e) 

soma = 0 

for i in range(0, len(elementos), posicoes):
    soma += elementos[i] 


print('Soma: {}.'.format(soma))    
