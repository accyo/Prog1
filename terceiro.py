# Terceiro Impar
soma = 0 
impar = 0

while impar < 3: 
    numero = int(input()) 
    
    soma += numero

    print("soma = {}".format(soma))

    if numero % 2 != 0:
        impar += 1

