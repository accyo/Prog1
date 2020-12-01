media_mensal = float(input())
acima_limite = []


while True: 
    gastos = []
    entrada = input()
    
    if entrada == 'fim':
        break
    
    else: 
        media = 0
        valores = entrada.split()
        
        for i in range(len(valores)):
            media += float(valores[i])
            gastos.append(float(valores[i]))
            
        if media > media_mensal:
            acima_limite.append(gastos)
            
        elif (media /len(valores)) < (media_mensal / 2):
            break

for gasto in range(len(acima_limite)):
    print(*acima_limite[gasto])
       
