# UFCG - PROG1 
# KAREN A. A. ALVES - 119210934
# Grep 

pc = input()             # palavra-chave 
N = int(input())         # quantidade de frases a serem lidas
tem_pc = False           # não possui a palavra-chave na frase 
                        

for frase in range(N):
    frase = input().split()

    if not tem_pc and pc == frase 
