# Bolsa do CNPq


meses = ['jan', 'fev', 'mar', 'abr', 'mai', 'jun', 'jul', 'ago', 'set', 'out', 'nov', 'dez'] 

gastos = []

bolsa = 500
 

for _ in range(12):             # Entrada - Gastos de cada mês
    gastos.append(int(input())) # Adicionar na lista de gastos


saldos = []         
saldo = 0   

for i in range(len(gastos)):

    saldo += bolsa - gastos[i]      # Acumulador pra verificar quanto saldo fica em cada mês
    saldos.append(saldo)            # Adiciona na lista de saldos
 
maior_saldo = saldos[0]             # Primeiro valor da lista de saldos é o maior saldo
melhor_mes = meses[0]                 # Primeiro mês da lista é o que tem maior saldo

for i in range(1, len(saldos)):     

    if saldos[i] >= maior_saldo:    # Se o saldo do mês for maior ou igual ao maior saldo (primeiro valor lido), a variável 'maior_saldo' é atualizada. 
        maior_saldo = saldos[i]
        melhor_mes = meses[i]       # String 'melhor_mes' é atualizada de acordo com a posição da variável 'maior_saldo'
        
print(melhor_mes) 

