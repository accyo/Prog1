# VALOR DE VENDA - U6

def calcula_venda(compra, ipi, iof, lucro):
    
    soma = compra * (ipi + iof + lucro)
    total = compra + soma
    return total
    

assert calcula_venda(50.0, 0.1, 0.1, 0.1) == 65.0
assert calcula_venda(80.0, 0.1, 0.3, 0.4) == 144.0
assert calcula_venda(60.0, 0.2, 0.5, 0.4) == 126.0

while True: 
    entrada = input()
    
    if entrada == '-':
        break
    
    else: 
        valores = entrada.split(",")
        
        print('O valor de venda para este produto deve ser R$ {:.2f}'.format(calcula_venda(float(valores[0]), float(valores[1]), float(valores[2]), float(valores[3]))))
