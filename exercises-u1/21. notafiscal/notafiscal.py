valor_total = float(input())
data = input()
qnt_de_produtos = input()

media = valor_total / float(qnt_de_produtos)
print('Data: {}'.format(data))
print('O valor total da compra foi de R$ {:.2f}. A média do preço dos produtos é de {:.1f}.'.format(valor_total, media))
