# Limite de Gastos

media_mensal = float(input()) # Limite gasto mensal (média)
acima_limite = []

while True:
    
    media = 0 
    ent = input()
    entrada = ent.split()
    
    if ent == 'fim':
        break
    
    else: 
        for i in range(len(entrada)):
            media += float(entrada[i])
        
        if (media / len(entrada)) > media_mensal: 
            acima_limite.append(ent)
            
        elif (media /len(entrada)) < (media_mensal / 2):
            break

        

for sequencia in acima_limite:
    print (sequencia)
