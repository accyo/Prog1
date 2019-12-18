digito = input()
num = int(digito[0]) + int(digito[1]) + int(digito[2]) + int(digito[3]) + int(digito[4])
total = num % int(11) 
print('{}-{:02d}'.format(digito, total))
