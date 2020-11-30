# Limite de Gastos

media_mensal = float(input()) # Limite gasto mensal (média)
acima_limite = []

while True:
    
    media = 0 
    e = input()     # entrada 
    entrada = e.split() # split da entrada 
    
    if e == 'fim':
        break
    
    else: 
        for i in range(len(entrada)):
            media += float(entrada[i])
        
        if (media/len(entrada)) > media_mensal:
            medias = ' '
                
            for i in range(len(entrada)):
                medias = float(entrada[i])
                acima_limite.append(str(medias))
            
        elif (media /len(entrada)) < (media_mensal / 2):
            break
          

        

print(*acima_limite)
