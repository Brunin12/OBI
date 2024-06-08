#!/usr/bin/env python3

class Bit:
    def __init__(self, n):
        self.size = n
        self.bit = [0]*(n + 1)

    def get(self, i):
        s = 0
        while i > 0:
            s += self.bit[i]
            i -= i & -i
        return s

    def add(self, i, x):
        while i <= self.size:
            self.bit[i] += x
            i += i & -i


def read_dist():
    x, y = map(int,input().split())
    return x*x + y*y


# Processa uma tupla (dist, idx) para descobrir a penalidade da flecha com
# identificador idx. Assumindo que as flechas serão processadas em ordem
# crescente de distância ao centro to alvo, para descobrir a penalidade da
# flecha idx basta contar quantas flechas com identificador menor que idx
# foram processadas até o momento.
def process(bit, tup):
    res = bit.get(tup[1])
    bit.add(tup[1], 1)
    return res


N = int(input())
# mapeia cada ponto da entrada para a tupla (distancia, identificador)
queries = [(read_dist(), i) for i in range(1, N+1)]

# ordena as flechas de acordo com a distância para o centro do alvo
queries.sort(key=lambda tup: tup[0])

bit = Bit(N)
ans = 0

# processa as flechas em ordem de distância
for item in queries:
    ans += process(bit, item)

print(ans)
