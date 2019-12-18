peso = float(input())
altura = float(input())

imc = peso / altura**2
peso_ideal = 24.9 * altura**2
gp = peso_ideal - peso

print('IMC atual = {:.2f}\nPeso a ser ganho/perdido = {:.2f}'.format(imc, gp))
