# Média Atinge Limite

medias = []

while True: 
    entrada = input()

    if entrada != '-':
            medias.append(entrada)

    else:
        break


limite = float(input())

elemento_maior_limite = 0
posicao = 0

for i in range(len(medias)):

    elemento_maior_limite += float(medias[i])
    posicao += 1
    media = elemento_maior_limite / posicao

    if media > limite: 
        
        elemento_maior_limite += float(medias[i])
        break

if limite >= media: 
    print("limite não alcançado")
else: 
    print("media = {:.1f}".format(media))
    print("num = {}".format(posicao))

