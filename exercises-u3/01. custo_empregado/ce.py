# UFCG - PROG1 
# KAREN A. A. ALVES - 119210934
# Custo Empregado

salario_bruto = float(input())       # Salário bruto do trabalhador
dias = int(input())                  # Quantidade de dias trabalhados
diario_transporte = float(input())   # Custo diário com transporte

# EMPREGADOR 
transporte = dias * diario_transporte   # Custo mensal do transporte
vale_transporte = salario_bruto * 0.06   # Vale transporte - 6% 
fgts = salario_bruto * 0.08         # FGTS descontado do salário do empregador - 8%
inss = salario_bruto * 0.12         # INSS descontado do salário do empregador - 12%
custo_mensal = salario_bruto + fgts + inss # Custo mensal a ser desembolsado pelo empregador


# INSS DO EMPREGADO 

if (salario_bruto <= 1317.07):      # Se o salário bruto for menor ou igual a R$ 1.317,07 
    aliquota = salario_bruto * 0.08
 # VALE TRANSPORTE
    if (transporte < vale_transporte):
        custo_mensal = salario_bruto + fgts + inss
        salario_liquido = salario_bruto - (aliquota + transporte)
    elif (transporte == vale_transporte):
        custo_mensal = salario_bruto + fgts + inss + vale_transporte
        salario_liquido = salario_bruto - aliquota
    elif (transporte > vale_transporte):
        custo_mensal = salario_bruto + fgts + inss + (transporte - vale_transporte)
        salario_liquido = salario_bruto - (aliquota + vale_transporte)

    print('salário bruto = R$ {:.2f}'.format(salario_bruto))
    print('custo mensal = R$ {:.2f}'.format(custo_mensal))
    print('salário líquido = R$ {:.2f}'.format(salario_liquido))

elif (salario_bruto >= 1317.08 and salario_bruto <= 2195.12):   # Se o salário bruto for entre R$ 1.317,08 e R$ 2.195,12
    aliquota = salario_bruto * 0.09
    if (transporte < vale_transporte):
        custo_mensal = salario_bruto + fgts + inss
        salario_liquido = salario_bruto - (aliquota + transporte)
    elif (transporte == vale_transporte):
        custo_mensal = salario_bruto + fgts + inss + vale_transporte
        salario_liquido = salario_bruto - aliquota
    elif (transporte > vale_transporte):
        custo_mensal = salario_bruto + fgts + inss + (transporte - vale_transporte)
        salario_liquido = salario_bruto - (aliquota +  vale_transporte)

    print('salário bruto = R$ {:.2f}'.format(salario_bruto))
    print('custo mensal = R$ {:.2f}'.format(custo_mensal))
    print('salário líquido = R$ {:.2f}'.format(salario_liquido))

elif (salario_bruto > 2195.13):                                 # Se o salário bruto for maior que R$ 2.195,13
    aliquota = salario_bruto * 0.11
    if (transporte < vale_transporte):
        custo_mensal = salario_bruto + fgts + inss
        salario_liquido = salario_bruto - (aliquota + transporte)
    elif (transporte == vale_transporte):
        custo_mensal = salario_bruto + fgts + inss + vale_transporte
        salario_liquido = salario_bruto - aliquota
    elif (transporte > vale_transporte):
        custo_mensal = salario_bruto + fgts + inss + (transporte - vale_transporte)
        salario_liquido = salario_bruto - (aliquota + vale_transporte)

    print('salário bruto = R$ {:.2f}'.format(salario_bruto))
    print('custo mensal = R$ {:.2f}'.format(custo_mensal))
    print('salário líquido = R$ {:.2f}'.format(salario_liquido))
