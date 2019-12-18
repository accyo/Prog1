# UFCG - PROG1 
# KAREN A. A. ALVES - 119210934
# CNPJ

raiz = input() 

soma_raiz = int(raiz[0]) + int(raiz[1]) + int(raiz[3]) + int(raiz[4]) + int(raiz[5]) + int(raiz[7]) +int(raiz[8]) + int(raiz[9])

verificador = soma_raiz + 1
print('{}.{}.{}/0001-{:02d}'.format(raiz[0:2], raiz[3:6], raiz[7:10], verificador))
