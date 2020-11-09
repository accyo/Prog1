# DESCARTA COINCIDENTES


n = int(input())

aceitos = []
descartados = []

for _ in range(n): 
    numeros = input() 
    cont = 0
    
    for i in range(len(numeros)):
        
        if i == int(numeros[i]):
            cont += 1

    if cont > 0: 
        descartados.append(numeros)

    else: 
        aceitos.append(numeros)

print("---")
print("{} aceito(s)".format(len(aceitos)))

for e in aceitos: 
    print(e)
print("{} descartado(s)".format(len(descartados)))

for e in descartados: 
    print(e)
