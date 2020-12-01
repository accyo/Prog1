# TIRO AO ALVO
import math 

distancia_media = []

while True:
    entrada = input().split(',')

    distancia = math.sqrt((float(entrada[0])**2) + (float(entrada[1])**2))    

    if distancia <= 200:
        distancia_media.append(distancia)
    else:
        break

acumulador_media = 0 

for pares in distancia_media: 
    print('{:.2f}'.format(pares))

for e in range(len(distancia_media)):
    acumulador_media += distancia_media[e]

if distancia_media != []: 

    media = acumulador_media / len(distancia_media)
    print('--')
    print('num disparos: {}'.format(len(distancia_media)))
    print('distancia media: {:.2f}'.format(media)) 

