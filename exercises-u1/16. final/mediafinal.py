print('== Estágio 1 ==')
peso1 = float(input('Peso? '))
nota1 = float(input('Nota? '))
print('== Estágio 2 ==')
peso2 = float(input('Peso? '))
nota2 = float(input('Nota? '))
print('== Estágio 3 ==')
peso3 = float(input('Peso? '))
nota3 = float(input('Nota? '))

media_parcial = (nota1*peso1)+(nota2*peso2)+(nota3*peso3)
nota_final_5 = (5.0 - (media_parcial * 0.6)) / 0.4 
nota_final_7 = (7.0 - (media_parcial * 0.6)) / 0.4

print('== Resultados ==')
print('Média parcial: {:.1f}\nNota na final, pra média 5.0 = {:.1f}\nNota na final, pra média 7.0 = {:.1f}'.format(media_parcial, nota_final_5, nota_final_7))
