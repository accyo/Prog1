num_adultos = int(input())
num_criancas = int(input())
preco_do_ingresso = float(input())

adultos = num_adultos * preco_do_ingresso
meia = preco_do_ingresso / 2 
criancas = num_criancas * meia 

total = adultos + criancas

print('Total: R$ {:.2f}'.format(total))
