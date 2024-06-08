# DEMORA TEMPO DEMAIS

import math

# Função para calcular a distância entre dois pontos
def calcular_distancia(p1, p2):
    return math.sqrt((p2[0] - p1[0]) ** 2 + (p2[1] - p1[1]) ** 2)

# Leitura da quantidade de flechas lançadas
quantidadeFlechasLancadas = int(input())

# Verificar se a quantidade de flechas está dentro do intervalo permitido
if quantidadeFlechasLancadas < 1 or quantidadeFlechasLancadas > 10 ** 5:
    exit()

# Lista para armazenar as coordenadas das flechas
coordenadasFlechas = []

# Leitura das coordenadas das flechas
for _ in range(quantidadeFlechasLancadas):
    x, y = map(int, input().split())
    if not (-10 ** 6 <= x <= 10 ** 6 and -10 ** 6 <= y <= 10 ** 6):
        exit()

    coordenadasFlechas.append((x, y))

# Ordenar as coordenadas das flechas com base na distância ao centro do alvo
coordenadasFlechas.sort(key=lambda p: calcular_distancia((0, 0), p))

# Inicializar a penalidade total como 0
penalidade_total = 0

# Contador de flechas mais próximas
flechas_mais_proximas = 0

# Calcular a penalidade para cada flecha
for flecha in coordenadasFlechas:
    distancia = calcular_distancia((0, 0), flecha)
    penalidade_total += flechas_mais_proximas
    if distancia != 0:
        flechas_mais_proximas += 1

# Imprimir a penalidade total
print(penalidade_total)
