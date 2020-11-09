# QUADRO DE MEDALHAS

medalhas_brasil = input().split()
medalhas_italia = input().split()

# CONTADOR DAS MEDALHAS 
ouro_brasil = 0
ouro_italia = 0 
prata_brasil = 0 
prata_italia = 0
bronze_brasil = 0 
bronze_italia = 0

# LAÇO PARA CONTAR O NUMERO DE MEDALHAS DE CADA PAÍS 


for i in range(len(medalhas_brasil)): 
    if int(medalhas_brasil[i]) == 0:
        ouro_brasil += 1
    if int(medalhas_brasil[i]) == 1:
        prata_brasil += 1
    if int(medalhas_brasil[i]) == 2: 
        bronze_brasil += 1 
    
for i in range(len(medalhas_italia)): 
    if int(medalhas_italia[i]) == 0: 
        ouro_italia += 1 
    if int(medalhas_italia[i]) == 1: 
        prata_italia += 1
    if int(medalhas_italia[i]) == 2: 
        bronze_italia += 1 

# COMPARAR O NUMERO DE MEDALHAS DE UM PAÍS COM O OUTRO 

if ouro_brasil == ouro_italia:      # CASO OS PAÍSES TENHA O MESMO NÚMERO DE MEDALHAS DE OURO   

    if prata_brasil > prata_italia: # COMPARAÇÃO DE MEDALHAS DE PRATA 
        print("brasil")

    elif prata_italia > prata_brasil: 
        print("italia")

    elif prata_brasil == prata_italia:
        if bronze_brasil > bronze_italia:   # COMPARAÇÃO DE MEDALHAS DE BRONZE
            print("brasil") 
        elif bronze_italia > bronze_brasil:
            print("italia")
        else: 
            print("empate")

elif ouro_brasil > ouro_italia: 
    print("brasil") 

elif ouro_italia > ouro_brasil: 
    print("italia")


