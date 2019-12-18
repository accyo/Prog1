# UFCG - PROG1
# KAREN A. A. ALVES
# Imprime Ranking (cumulativo)

n = int(input())
times = []       # Times
pontos = []     # Pontuação de cada times
ranking = 1    # Posição 

for i in range(n): 
    times.append(input())
    pontos.append(input())
    

for i in range(n):
    if i == 0:
        print('{}. {} ({})'.format(ranking, times[0], pontos[0]))

    elif pontos[i] == pontos[i-1]:
        print('{}. {} ({})'.format(ranking, times[i], pontos[i]))

    else:
        ranking = i + 1
        print('{}. {} ({})'.format(ranking, times[i], pontos[i]))

