graus = int(input())
minutos = int(input())
segundos = int(input())

minut  = minutos/ 60
seg = segundos/ 3600

graus_decimais = graus+minut+seg
print('graus = {:.4f}'.format(graus_decimais))
