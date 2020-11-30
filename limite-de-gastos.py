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
            for i in range(len(entrada)):           
                acima_limite.append(float(entrada[i]))
            
        elif (media /len(entrada)) < (media_mensal / 2):
            break


        

print(*acima_limite)
