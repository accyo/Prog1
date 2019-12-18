# UFCG
# PROG1 
# KAREN A. A. ALVES - 119210934

# Tweets por página 

tweets = int(input())  # entrada do número de tweets
pagina = tweets // 400 # número de páginas 
resto = tweets % 400  # tweets perdidos
tweets_perdidos = (resto * 100) / tweets


print('Serão necessárias {} página(s) para visualizar os tweets.'.format(pagina))
print('{:.1f}% dos tweets serão perdidos.'.format(tweets_perdidos))
