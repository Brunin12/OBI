kms_rodados = int(input())
if (kms_rodados < 6 | kms_rodados > 800008):
    exit()

distancia = kms_rodados - 3

d = distancia % 8

mapa_sensores = {0: 1, 1: 2, 2: 3, 3: 1, 4: 2, 5: 3, 6: 1, 7: 2, 8: 3}

print(mapa_sensores[d])


