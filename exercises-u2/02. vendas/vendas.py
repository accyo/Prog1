# UFCG
# Prog1 
# Karen A. A. Alves

num_brinq = int(input())        # Brinquedos vendidos no mês
brinq_teresa = int(input())     # Brinquedos vendidos no mês por Teresa 
brinq_carla = int(input())      # Brinquedos vendidos no mês por Carla 

teresa_total = num_brinq - brinq_teresa
carla_total = num_brinq - brinq_carla
joaquim_total = num_brinq - brinq_teresa - brinq_carla

por_teresa = (brinq_teresa / num_brinq) * 100 
por_carla = (brinq_carla / num_brinq) * 100
por_joaquim = (joaquim_total / num_brinq) * 100

print("Teresa vendeu {} (de {}) brinquedos. ({:.2f}%)".format(brinq_teresa, num_brinq, por_teresa))
print("Joaquim vendeu {} (de {}) brinquedos. ({:.2f}%)".format(joaquim_total, num_brinq, por_joaquim))
print("Carla vendeu {} (de {}) brinquedos. ({:.2f}%)".format(brinq_carla, num_brinq, por_carla))
