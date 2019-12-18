# UFCG - PROG1
# KAREN A. A. ALVES - 11210934
# Ataque Mais Positivo de um Campeonato

num_times = int(input())    # número de times

times = []                   # lista p/ armazenar os times
gols = []                   # lista p/ numero de gols de cada time
melhor_ataque = 0           
melhor_time = ''
soma = 0

for e in range(num_times):  
    times.append(input())
    gols.append(int(input()))

    if e == 0:
        melhor_ataque = gols[e]
        melhor_time = times[e]  

    elif (gols[e] > melhor_ataque):
        melhor_ataque = gols[e]  
        melhor_time = times[e]

for gol in range(len(gols)):
    soma += gols[gol]


media = soma / num_times


print('Time(s) com melhor ataque ({} gol(s)):'.format(melhor_ataque))
print(melhor_time)
print('Média de gols marcados: {:.1f}'.format(media))
