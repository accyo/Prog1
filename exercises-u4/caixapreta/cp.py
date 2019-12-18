# UFCG - PROG1 
# KAREN A. A. ALVES - 119210934
# Caixa Preta


qnt = int(input())
validos = 0
invalidos = 0

for i in range(qnt):
    n = input().split()
    
    if invalidos == 0:
        for e in range(len(n)):
            if int(n[e]) >= 0:
                validos += 1
            else: 
                break

    if invalidos == 0:
        if int(n[0]) < 0:
            print ('dado inconsistente. peso negativo.')
            invalidos += 1
            
        elif int(n[1]) < 0:
            print('dado inconsistente. combustível negativo.')
            invalidos += 1
            
        elif int(n[2]) < 0:
            print('dado inconsistente. altitude negativa.')
            invalidos +=1

print('{} dados válidos.'.format(validos))           
