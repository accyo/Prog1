# DIGITO POR DIGITO

n = int(input())

digitos = [] 

while True: 

    digito = n % 10
    digitos.append(digito)

    resto = n // 10
    n = resto 

    if n <= 0:
        
        break


for e in digitos:
    print(e)


