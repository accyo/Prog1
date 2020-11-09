# TST - MT da Unidade 4. 
# ENCONTROS VOCALICOS
# Faça um código que verifique quais das palavras tem encontro vocálicos e quais não têm. 
# Encontros vocálicos são palavras que possuem mais de uma vogal consecutiva. Exemplo: maioria, simpatia, biblioteca. 

quant_palavras = int(input())           # Quantas palavras serão lidas

com_vogais = []         # Lista para armazenar as palavras que possuem encontros vocálicos
sem_vogais = []         # Lista para armazenar as palavras que NÃO possuem encontros vocálicos

for palavra in range(quant_palavras):   # Laço com range na quantidade de palavras
    palavra = input()
    cont = 0                # Contador de vogais
    
    for e in range(len(palavra)):   # Um outro laço para percorrer elemento por elemento na palavra
      # A condição se o elemento tiver vogal na posição anterior e atual, contamos +1 no contador. 
        if palavra[e-1] in 'aeiou':     
            if palavra[e] in 'aeiou':
          
                cont += 1       # Esse contador é apenas uma espécie de "flag" para add a palavra na lista correspondente. 
                
    if cont >= 1:               # Se o contador for maior ou igual a 1, a palavra entra na lista de encontros vocálicos. 
        com_vogais.append(palavra)
    
    else:    
        sem_vogais.append(palavra) # Caso não, entra na outra lista. 
        
            
            
            
            
        
            
