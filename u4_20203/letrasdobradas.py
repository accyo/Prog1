# PALAVRAS COM LETRAS DOBRADAS


N = int(input())

palavrasdobradas = []
palavras_naodobradas = [] 


for _ in range(N): 
    
    dobradas = 0 

    palavras = input() 
    
    for i in range(1, len(palavras)): 

        if palavras[i-1] == palavras[i]: 
            dobradas += 1
    
    if dobradas > 0: 
    
        palavrasdobradas.append(palavras)

    else:
        palavras_naodobradas.append(palavras)


print("{} palavra(s) com letras dobradas:".format(len(palavrasdobradas)))

for palavra in palavrasdobradas: 
    print (palavra)

print("---")

print("{} palavra(s) sem letras dobradas:".format(len(palavras_naodobradas)))

for palavra in palavras_naodobradas:
    print (palavra)

