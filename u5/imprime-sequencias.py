# Imprime Sequencias - Unidade5 (Não terminado)

alvo = int(input())
seq = 0

while True: 
    
    entrada = input()
    seq += 1
    if entrada != "fim":
        entradas = entrada.split()
        sequencias = []
    
        cont = 0
        for i in range(len(entradas)): 
            if int(entradas[i]) > alvo: 
                cont += 1
        if cont > (len(entradas))//2: 
            print('sequencia{}: {}'.format(seq, entrada))
    else:
        break
    
