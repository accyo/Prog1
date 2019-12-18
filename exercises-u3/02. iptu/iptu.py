# UFCG - PROG1
# KAREN A. A. ALVES - 119210934
# IPTU

area = float(input()) # área construída da propriedade
valor_metro = float(input()) # valor do metro quadrado na região
pagamento = input()     # a vista, 2x ou 3x
imposto = area * valor_metro    # cálculo para saber o valor do imposto

if (pagamento == 'vista'): 
    total = imposto - (imposto * 0.2)
    print('Total: R$ {:.2f}'.format(total))
elif (pagamento == '2x'):
    total = imposto - (imposto * 0.1)
    parcelas = total / 2 
    print('Total: R$ {:.2f}. Parcelas: R$ {:.2f}'.format(total, parcelas))

elif (pagamento == '3x'): 
    total = imposto - (imposto * 0.05)
    parcelas = total / 3 
    print('Total: R$ {:.2f}. Parcelas: R$ {:.2f}'.format(total, parcelas))
