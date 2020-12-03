# Teste 

lista = ['casa', 'abacate', 'boi', 'casa', 'jornal', 'elo', 'faca'] 
nova_lista = []

for palavra in range(1, len(lista), 2):
        
    if lista[palavra-1] > lista[palavra]:
        nova_lista.append(lista[palavra])
        nova_lista.append(lista[palavra-1])
    
    elif lista[palavra] > lista[palavra-1]:
        nova_lista.append(lista[palavra-1])
        nova_lista.append(lista[palavra])
        

            
     
    
    

        
    
