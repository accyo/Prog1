#Ataque Mais Positivo de um Campeonato

numero_de_times = int(input())
times_melhor_ataque = []        # Lista para armazenar os times com melhor ataque


melhor_time = input()
times_melhor_ataque.append(melhor_time)     # Primeiro Time é considerado o melhor time 

melhor_ataque = int(input())  # Primeiro ataque é considerado o melhor ataque

soma = melhor_ataque  # A soma começa o valor dos gols do primeiro time 



for i in range(1, numero_de_times):
    times = input()
    gols = int(input())
    soma += gols            # Somatorio de gols de todos os times

    if melhor_ataque == gols:   # Se o melhor ataque for igual ao gols, o time entra na lista de times com melhores ataques
        times_melhor_ataque.append(times)

    elif melhor_ataque < gols: 
        times_melhor_ataque = []    # Se o melhor ataque for menor que o gols do time lido, a lista é esvaziada. 
        melhor_ataque = gols    # Se número de gols for maior que o do melhor ataque, o melhor ataque será substituido pelo número de gols. 
        melhor_time = times     # assim como o melhor time 
        times_melhor_ataque.append(times)   # O time com melhor ataque é adicionado na lista de times com melhor ataque. 


print("Time(s) com melhor ataque ({} gol(s)):".format(melhor_ataque))

for times in times_melhor_ataque: 
    print (times)

media = soma / numero_de_times

print("\nMédia de gols marcados: {:.1f}".format(media))

