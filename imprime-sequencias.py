# Imprime Sequencias - Unidade5 (Não terminado)

alvo = int(input())
seq = 0

while True: 
    
    entrada = input().split()
    if entrada != "fim":
        sequencias = []
        cont = 0
        for i in range(len(entrada)): 
            if int(entrada[i]) > alvo: 
                cont += 1
            if cont > (len(entrada))//2: 
                sequencias.append(int(entrada[i]))
        
                for _ in entrada: 
                    print(_, end='')
