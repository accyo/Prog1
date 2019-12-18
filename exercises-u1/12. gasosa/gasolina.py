pos_inicial = float(input())
litros_inicial = float(input())
pos_final = float(input())
litros_final = float(input())

dist = pos_final - pos_inicial
delta = litros_inicial - litros_final
consumo = dist / delta 

print('{:.1f}'.format(consumo))
