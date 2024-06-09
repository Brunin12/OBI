# Ler a distância total D
D = int(input().strip())

# Determinar o sensor com base no resto da divisão por 8 do valor (D - 3)
sensor = {0: 1, 1: 2, 2: 3, 3: 1, 4: 2, 5: 3, 6: 1, 7: 2}[(D - 3) % 8]

# Imprimir o sensor atingido
print(sensor)
