# UFCG - PROG1 
# KAREN A. A. ALVES - 119210934
# Converte Senha

senha = input()         # Senha normal
nova_senha = senha[0]   # Variável da senha codificada
trocas = 0              # Contador de trocas

for i in range(1, len(senha)):  # Laço for para cada índice da senha (começando pelo segundo índice)
    letra = senha[i].lower()     # variavél para encontrar as vogais na senha | Função 'lower.()' para deixar as letras minúsculas

    if letra == 'a':            # condições 
        nova_senha += '4'       # acumulador para substituir cada vogal 'a' por '4'
        trocas += 1             # acumulador do número de trocas na senha

    elif letra == 'e':
        nova_senha += '3'       # acumulador para substituir cada vogal 'e' por '3'
        trocas += 1         
        
    elif letra == 'i':          # acumulador para substituir cada vogal 'i' por '1'
        nova_senha += '1'
        trocas += 1
        
    elif letra == 'o':          # acumulador para substituir cada vogal 'o' por '0' 
        nova_senha += '0'
        trocas += 1

    else:                       # caso não seja necessário trocar as letras, repete cada letra
        nova_senha += senha[i]

print('{} ({} troca(s))'.format(nova_senha, trocas))

