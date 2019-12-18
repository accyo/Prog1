potencia = int(input())     # potência em Watts
tempo = int(input())        # minutos 

c_tempo = tempo / 60        # conversão de minutos para hora.
kwh = (potencia * c_tempo) / 1000 
print ('{:.1f} kWh'.format(kwh))

