# CAMPANHA 

# CONTADORES 

vitorias = 0    # VITORIAS DO CAMPINENSE
empates = 0     # EMPATES   
derrotas = 0    # DERROTAS  '' 

pontos_Casa = 0     # GOLS DO CAMPINENSE EM CASA 
pontos_Fora = 0     # GOLS DO CAMPINENSE FORA DE CASA 

gols_Pro = 0        # GOLS DO CAMPINENSE
gols_Contra = 0     # GOLS DO OUTRO TIME


for _ in range(10):     # ENTRADA DOS JOGOS
    jogos = input()
    placar = jogos.split() 
    

# CONDIÇÕES - JOGOS EM CASA 

    if placar[1][1] == 'c':
       
        gols_Pro += int(placar[0][0]) 
        gols_Contra += int(placar[0][2])
        
        if int(placar[0][0]) > int(placar[0][2]): 
            vitorias += 1
            pontos_Casa += 3

        elif int(placar[0][0]) == int(placar[0][2]): 
            empates += 1
            pontos_Casa += 1  
        
        else:
            derrotas += 1                


# CONDIÇÕES - JOGOS FORA DE CASA 

    if placar[1][1] == 'f': 

       gols_Pro += int(placar[0][2])
       gols_Contra += int(placar[0][0])

       if int(placar[0][0]) > int(placar[0][2]): 
            derrotas += 1
        
       elif int(placar[0][0]) == int(placar[0][2]): 
            empates += 1
            pontos_Fora += 1

       else:
            vitorias += 1
            pontos_Fora += 3

saldo = gols_Pro - gols_Contra
pontos = (vitorias*3) + empates

print("{}v, {}e, {}d".format(vitorias, empates, derrotas))
print("pontos: {}".format(pontos))
print("saldo: {} ({} pro, {} contra)".format(saldo, gols_Pro, gols_Contra))
print("pontos em casa: {}".format(pontos_Casa))
print("pontos fora: {}".format(pontos_Fora))
