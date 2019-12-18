qnt_graodesoja = int(input())
qnt_clientes_atacado = int(input())
qnt_clientes_varejo = int(input())
resto_soja = qnt_graodesoja % qnt_clientes_atacado
print('Clientes no atacado = {}kg cada.'.format(qnt_graodesoja // qnt_clientes_atacado))
print('Clientes no varejo = {:.2f}kg cada.'.format(resto_soja / qnt_clientes_varejo))
