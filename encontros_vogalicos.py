# TST - MT da Unidade 4. 
# ENCONTROS VOCALICOS
# Faça um código que verifique quais das palavras tem encontro vocálicos e quais não têm. 
# Encontros vocálicos são palavras que possuem mais de uma vogal consecutiva. Exemplo: maioria, simpatia, biblioteca. 

quant_palavras = int(input())

com_vogais = []
sem_vogais = [] 

for palavra in range(quant_palavras):
    palavra = input()
    cont = 0 
    
    for e in range(len(palavra)): 
      
        if palavra[e-1] in 'aeiou':
            if palavra[e] in 'aeiou':
          
                cont += 1
                
    if cont > 1:  
        com_vogais.append(palavra)
    
    else:    
        sem_vogais.append(palavra)
        
            
            
            
            
        
            
