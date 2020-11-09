# MAIS CONSOANTES
cont = 0 

while True: 
    palavra = input().lower()
    vogais = 0
    consoantes = 0
    for e in range(len(palavra)):

        if palavra[e] in 'aeiou': 
            vogais += 1 
        if palavra[e] not in 'aeiou': 
            consoantes += 1

    if consoantes > vogais: 
        cont += 1 
        break
    
    else: 
        cont += 1
print(cont)
