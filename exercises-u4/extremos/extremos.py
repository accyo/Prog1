# UFCG - PROG1
# KAREN A. A. ALVES - 119210934
# Classificação de Elementos Utilizando a Média dos Extremos

n = int(input())
numeros = [] 
maior = 0
menor = 0

for e in range(n):
    num = int(input())
    if e == 0:
        maior = num
        menor = num 
    elif (num > maior):
        maior = num
    elif (num < menor):
         menor = num

    numeros.append(num)

media = (maior + menor) / 2.0

acima_media = 0
abaixo_media = 0

for num in numeros: 
    if (num < media):
        abaixo_media += 1
    if (num > media):
         acima_media += 1 

print('Menor número: {}'.format(menor))
print('Maior número: {}'.format(maior))
print('Média dos extremos: {:.2f}'.format(media))
print('{} número(s) abaixo da média'.format(abaixo_media))
print('{} número(s) acima da média'.format(acima_media))
